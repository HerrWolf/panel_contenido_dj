import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from core.dashboard.forms import MovieForm
from core.dashboard.helpers.movie.helpers import get_subs_movie_category_id
from core.dashboard.models import Movie, Category
from core.media_downloader import MediaDownloader

from icecream import ic


@login_required
def movie_list_view(request):
    page = int(request.GET.get('page', 1))
    search_query = request.GET.get('search', '')
    page_size = 10

    all_movies = Movie.objects.all().order_by('-id')
    if search_query:
        all_movies = all_movies.filter(
            Q(title__icontains=search_query) |
            Q(original_title__icontains=search_query) |
            Q(tmdb_id__icontains=search_query)
        )

    start_index = (page - 1) * page_size
    end_index = page * page_size
    movies = all_movies[start_index:end_index]
    has_more = all_movies.count() > end_index

    # If it's an HTMX request
    if request.headers.get('HX-Request') and not (request.GET.get('create') or request.GET.get('edit')):
        return render(request, 'movie/partials/movie-rows.html', {
            'movies': movies,
            'has_more': has_more,
            'next_page': page + 1,
            'search': search_query
        })

    form = MovieForm()

    # Si es una solicitud HTMX para cargar el modal de creacion
    if request.htmx and request.GET.get('create'):
        form_url = reverse_lazy('movie-create-view')
        data = {
            'form': form,
            'form_url': form_url,
            'modal_title': 'Agregar Película'
        }
        return render(request, 'movie/partials/form-movie.html', data)

    # Si es una solicitud HTMX para cargar el modal de edición
    if request.htmx and request.GET.get('edit'):
        movie = Movie.objects.get(pk=request.GET.get('edit'))
        form = MovieForm(instance=movie)
        form_url = reverse_lazy('movie-edit-view', kwargs={'pk': movie.pk})
        data = {
            'form': form,
            'movie': movie,
            'form_url': form_url,
            'modal_title': 'Editar Película'
        }
        return render(request, 'movie/partials/form-movie.html', data)

    data = {
        'title': 'Listado de Películas',
        'table_title': 'Listado de Películas',
        'list_url': reverse_lazy('movie-list-view'),
        'entity': 'Películas',
        'table_id': 'tbl_movie',
        'movies': movies,
        'form': form,
        'has_more': has_more,
        'next_page': page + 1
    }

    return render(request, 'movie/movie-list.html', data)


@login_required
def fetch_movie_by_id(request):
    tmdb_id = request.GET.get('tmdb_id', '')

    if not tmdb_id or not tmdb_id.isdigit():
        return HttpResponse(json.dumps({'error': 'ID inválido'}), content_type='application/json')

    try:
        downloader = MediaDownloader()
        movie_data = downloader.get_details_by_id('movie', int(tmdb_id))

        print(json.dumps(movie_data))

        # Crear un objeto JSON con la información requerida
        response_data = {
            'tmdb_id': movie_data['id'],
            'title': movie_data['title'],
            'original_title': movie_data['original_title'],
            'poster_url': f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path', '')}",
            'backdrop_url': f"https://image.tmdb.org/t/p/original{movie_data.get('backdrop_path', '')}",
            'overview': movie_data['overview'],
            'release_date': movie_data['release_date'],
            'categories': movie_data['genres'],
        }

        # Devolver directamente la respuesta JSON
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({'error': str(e)}), content_type='application/json')


@login_required
def search_movies_by_title(request):
    title = request.GET.get('title', '')

    if not title:
        return HttpResponse(json.dumps([]), content_type='application/json')

    try:
        downloader = MediaDownloader()
        results = downloader.search_by_name('movie', title)

        # Format the results for the frontend
        formatted_results = []
        for movie in results[:10]:
            formatted_results.append({
                'tmdb_id': movie['id'],
                'title': movie['title'],
                'original_title': movie.get('original_title', ''),
                'release_date': movie.get('release_date', ''),
                'poster_path': f"https://image.tmdb.org/t/p/w92{movie.get('poster_path', '')}" if movie.get(
                    'poster_path') else ''
            })

        return HttpResponse(json.dumps(formatted_results), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps({'error': str(e)}), content_type='application/json', status=400)


@login_required
def movie_create_view(request):
    if request.method == 'POST':
        ic(request.POST)
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.instance
            selected_categories = form.cleaned_data['categories']
            audio = form.cleaned_data['audio']

            new_categories = []
            if audio == 'sub':
                last_added = Category.objects.get(pk=85)
                new_categories.append(last_added.id)
                for category in selected_categories:
                    if category.name == 'Mexicanas':
                        continue
                    category_subs = get_subs_movie_category_id(category.name)
                    new_categories.append(category_subs)
                form.cleaned_data['categories'] = new_categories
            else:
                recien_agregadas = Category.objects.get(pk=1)
                new_categories.append(recien_agregadas.id)
                for category in selected_categories:
                    form.cleaned_data['categories'] = category.id

            form.save()
            response = render(request, 'movie/partials/movie-row.html', {'movie': movie})
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Película creada con éxito",
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
                    "message": "Error al crear la película",
                    "title": "Operación fallida",
                    "type": "error"
                }
            })
            return response
    return redirect('movie-list-view')


@login_required
def movie_edit_view(request, pk):
    movie = Movie.objects.get(pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            movie = form.instance
            response = render(request, 'movie/partials/movie-row.html', {'movie': movie})
            response['HX-Trigger'] = json.dumps({
                "close-modal": None,
                "show-toast": {
                    "message": "Película actualizada con éxito",
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
                    "message": "Error al actualizar la película",
                    "title": "Operación fallida",
                    "type": "error"
                }
            })
            return response

    return redirect('movie-list-view')



@login_required
@require_http_methods(["DELETE"])
def movie_delete_view(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        response = HttpResponse(status=204)
        response['HX-Trigger'] = json.dumps({
            "show-toast": {
                "message": "Película eliminada con éxito",
                "title": "Operación exitosa",
                "type": "success"
            }
        })
        return response

    except Movie.DoesNotExist:
        response = JsonResponse({"error": "Película no encontrada"}, status=404)
        response['HX-Trigger'] = json.dumps({
            "show-toast": {
                "message": "Película no encontrada",
                "title": "Operación fallida",
                "type": "error"
            }
        })
        return response









