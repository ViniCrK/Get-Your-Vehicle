from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    cpf = forms.CharField(
        max_length=14, help_text='Insira seu CPF sem ponto(.) ou hífen(-)')
    celular = forms.CharField(max_length=14)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2',)
