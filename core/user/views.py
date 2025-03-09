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