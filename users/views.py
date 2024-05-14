from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
