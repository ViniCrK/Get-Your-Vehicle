from django.views.generic import View, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'site_title': "Cadastro de Usuário"
        })

        return context


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('vehicles/list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'site_title': "Autenticação de Usuário"
        })

        return context
