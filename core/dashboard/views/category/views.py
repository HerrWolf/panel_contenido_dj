import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from core.dashboard.forms import CategoryForm
from core.dashboard.models import Category


@login_required
def category_list_view(request):
    page = int(request.GET.get('page', 1))
    search_query = request.GET.get('search', '')
    page_size = 10  # Número de categorías por página

    # Filter categories by search query if provided
    all_categories = Category.objects.all().order_by('-id')
    if search_query:
        all_categories = all_categories.filter(
            Q(name__icontains=search_query) |
            Q(content_type__name__icontains=search_query) |
            Q(id__icontains=search_query)
        )

    # Calculate pagination
    start_index = (page - 1) * page_size
    end_index = page * page_size
    categories = all_categories[start_index:end_index]
    has_more = all_categories.count() > end_index

    # If it's an HTMX request
    if request.headers.get('HX-Request') and not (request.GET.get('create') or request.GET.get('edit')):
        return render(request, 'category/partials/category-rows.html', {
            'categories': categories,
            'has_more': has_more,
            'next_page': page + 1,
            'search': search_query
        })

    form = CategoryForm()

    # Si es una solicitud HTMX para cargar el modal de creacion
    if request.htmx and request.GET.get('create'):
        form_url = reverse_lazy('category-create-view')
        data = {
            'form': form,
            'form_url': form_url,
            'modal_title': 'Agregar Categoria'
        }
        return render(request, 'category/partials/form-category.html', data)

    # Si es una solicitud HTMX para cargar el modal de edición
    if request.htmx and request.GET.get('edit'):
        category = Category.objects.get(pk=request.GET.get('edit'))
        form = CategoryForm(instance=category)
        form_url = reverse_lazy('category-edit-view', kwargs={'pk': category.pk})
        data = {
            'form': form,
            'category': category,
            'form_url': form_url,
            'modal_title': 'Editar Categoria'
        }
        return render(request, 'category/partials/form-category.html', data)

    data = {
        'title': 'Listado de Categorias',
        'table_title': 'Listado de Categorias',
        'list_url': reverse_lazy('category-list-view'),
        'entity': 'Categorias',
        'table_id': 'tbl_category',
        'categories': categories,
        'form': form,
        'has_more': has_more,
        'next_page': page + 1
    }

    return render(request, 'category/category-list.html', data)


@login_required
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category = form.instance
            response = render(request, 'category/partials/category-row.html', {'category': category})
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Categoria creada con éxito",
                    "title": "Operación exitosa",
                    "type": "success"
                }
            })
            return response
        else:
            errors = {field: error for field, error in form.errors.items()}
            response = JsonResponse({"errors": errors}, status=400)
            response['HX-Trigger'] = json.dumps({
                "show-toast": {
                    "message": "Error al crear la categoria",
                    "title": "Operación fallida",
                    "type": "error"
                }
            })
            return response
    return redirect('category-list-view')


def category_edit_view(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            category = form.instance
            response = render(request, 'category/partials/category-row.html', {'category': category})
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Categoria actualizada con éxito",
                    "title": "Operación exitosa",
                    "type": "success"
                }
            })
            return response
        else:
            errors = {field: error for field, error in form.errors.items()}
            response = JsonResponse({"errors": errors}, status=400)
            response['HX-Trigger'] = json.dumps({
                "show-toast": {
                    "message": "Error al actualizar la categoria",
                    "title": "Operación fallida",
                    "type": "error"
                }
            })
            return response
    return redirect('category-list-view')


@login_required
@require_http_methods(["DELETE"])
def category_delete_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        response = HttpResponse(status=204)
        response['HX-Trigger'] = json.dumps({
            "show-toast": {
                "message": "Categoria eliminada con éxito",
                "title": "Operación exitosa",
                "type": "success"
            }
        })
        return response

    except Category.DoesNotExist:
        response = JsonResponse({"error": "Categoria no encontrada"}, status=404)
        response['HX-Trigger'] = json.dumps({
            "show-toast": {
                "message": "Categoria no encontrada",
                "title": "Operación fallida",
                "type": "error"
            }
        })
        return response
