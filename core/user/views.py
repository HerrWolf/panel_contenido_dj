import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from core.user.forms import UserForm
from core.user.models import User


@login_required
def user_list_view(request):
    users = User.objects.all().order_by('-id')
    newUserForm = UserForm()

    if request.method == "POST" and request.htmx:
        newUserForm = UserForm(request.POST, request.FILES)
        if newUserForm.is_valid():
            newUserForm.save()
            newUser = newUserForm.instance

            # Respuesta exitosa con mensaje de éxito
            response = render(request, 'user/partials/new_user_row.html', {'user': newUser})
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Usuario creado con éxito",
                    "title": "Operación exitosa",
                    "type": "success"
                }
            })
            return response
        else:
            # Manejo de errores: Devolver errores del formulario
            errors = {field: error for field, error in newUserForm.errors.items()}
            response = JsonResponse({"errors": errors}, status=400)
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Error al crear el usuario",
                    "title": "Operación fallida",
                    "type": "error"
                }
            })
            return response

    # Si es una solicitud HTMX para cargar el modal de edición
    if request.htmx and request.GET.get('create'):
        form = UserForm()
        return render(request, 'user/partials/form-create-user.html', {'form': form})

    if request.htmx and request.GET.get('edit'):
        user = User.objects.get(pk=request.GET.get('edit'))
        form = UserForm(instance=user)
        return render(request, 'user/partials/form-edit-user.html', {'form': form, 'user': user})

    data = {
        'title': 'Listado de Usuarios',
        'table_title': 'Listado de Usuarios',
        'list_url': reverse_lazy('user_list'),
        'entity': 'Usuarios',
        'table_id': 'tbl_user',
        'users': users,
        'form': newUserForm,
    }
    return render(request, 'user/list.html', data)


@login_required
def user_edit_view(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # Renderizar el registro actualizado
            response = render(request, 'user/partials/new_user_row.html', {'user': user})
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Usuario actualizado con éxito",
                    "title": "Operación exitosa",
                    "type": "success"
                }
            })
            return response
        else:
            # Manejo de errores
            errors = {field: error for field, error in form.errors.items()}
            response = JsonResponse({"errors": errors}, status=400)
            response['HX-Trigger'] = json.dumps({
                "show-toast": {
                    "message": "Error al actualizar el usuario",
                    "title": "Operación fallida",
                    "type": "error"
                }
            })
            return response
    else:
        form = UserForm(instance=user)

    return render(request, 'user/partials/modal-user.html', {'form': form, 'user': user})


@login_required
@require_http_methods(["DELETE"])
def user_delete_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        response = HttpResponse(status=204)
        response['HX-Trigger'] = json.dumps({
            "show-toast": {
                "message": "Usuario eliminado con éxito",
                "title": "Operación exitosa",
                "type": "success"
            }
        })
        return response
    except User.DoesNotExist:
        response = JsonResponse({"error": "Usuario no encontrado"}, status=404)
        response['HX-Trigger'] = json.dumps({
            "show-toast": {
                "message": "Usuario no encontrado",
                "title": "Operación fallida",
                "type": "error"
            }
        })
        return response
