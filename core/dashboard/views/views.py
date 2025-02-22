from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from core.app1_fuss.models import User as UserApp1Fuss, Users2 as User2App1Fuss, Contenido
from core.xui.models import Users as XuiUsers

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


def test(request):
    users = XuiUsers.objects.all()
    users_list = list(users.values())

    data = {
        'count': users.count(),
        'users': users_list,
    }

    return JsonResponse(data)
