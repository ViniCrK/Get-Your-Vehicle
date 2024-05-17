from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = 'vehicles/list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'site_title': "Cadastro de Usuário"
        })

        return context
