from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from core.mixins import ValidatePermissionRequiredMixin
from core.user.forms import UserForm
from core.user.models import User


# Create your views here.
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'
    form = UserForm

    # permission_required = 'user.view_user'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['table_title'] = 'Listado de Usuarios'
        context['create_url'] = reverse_lazy('user_create')
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('user_list')
        context['table_id'] = 'tbl_user'
        context['form'] = self.form
        return context


@login_required
def user_list_view(request):

    users = User.objects.all().order_by('-id')
    newUserForm = UserForm()

    if request.method == "POST" and request.htmx:
        newUserForm = UserForm(request.POST, request.FILES)
        if newUserForm.is_valid():
            newUserForm.save()
            newUser = newUserForm.instance
            response = render(request, 'user/partials/new_user_row.html', {'user': newUser})
            response['HX-Trigger'] = 'close-modal'
            return response


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


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('user_list')
    # permission_required = 'user.add_user'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                with transaction.atomic():
                    form = self.get_form()
                    data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

