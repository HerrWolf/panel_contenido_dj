from django.db import transaction
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.utils import get_search_parameter
from core.app1_fuss.models import User as UserApp1Fuss, Users2 as User2App1Fuss, Contenido as App1FussContenido, \
CatCategorias as App1FussCatCategorias
# from core.xui.models import Users as XuiUsers
from core.xui_one.models import StreamsCategories as XuiOneStreamsCategories
from core.dashboard.choices import *
from core.media_downloader import MediaDownloader


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


def testAddCategory(request):
    with transaction.atomic():
        category = XuiOneStreamsCategories()
        category.category_type = 'live'
        category.category_name = 'Test category 3'
        category.parent_id = 0
        category.cat_order = 99
        category.is_adult = 0
        category.save()

    data = {
        'status': 'ok',
        'id': category.id,
    }

    return JsonResponse(data)

def testDeleteCategory(request, id):
    with transaction.atomic():
        category = XuiOneStreamsCategories.objects.get(id=id)
        category.delete()

    data = {
        'status': 'ok',
    }

    return JsonResponse(data)

def test(request):
    categories = XuiOneStreamsCategories.objects.all()
    categories_list = list(categories.values())

    data = {
        'count': categories.count(),
        'categories': categories_list,
    }

    return JsonResponse(data)

def testGetCategories(request):
    categorias = App1FussCatCategorias.objects.all()
    categorias_list = list(categorias.values())

    data = {
        'count': categorias.count(),
        'categorias': categorias_list,
    }

    return JsonResponse(data)


def testSearchMovieData(request, content_type, query):
    md = MediaDownloader()
    search_param = get_search_parameter(query)
    results = md.download_media_info(content_type, search_param)

    data = {
        'status': 'ok',
        'count': len(results),
        'results': results,
    }
    return JsonResponse(data)


def testSeasonInfo(request, series_id, season_number):
    md = MediaDownloader()
    season_info = md.get_season_details(series_id, season_number)

    data = {
        'status': 'ok',
        'season_info': season_info,
    }
    return JsonResponse(data)

def testEpisodeInfo(request, series_id, season_number, episode_number):
    md = MediaDownloader()
    episode_info = md.get_episode_details(series_id, season_number, episode_number)

    data = {
        'status': 'ok',
        'episode_info': episode_info,
    }
    return JsonResponse(data)
