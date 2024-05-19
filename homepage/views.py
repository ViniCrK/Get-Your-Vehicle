from django.shortcuts import render


def home(request):
    context = {
        'site_title': 'Página Inicial'
    }
    return render(request, 'homepage/home.html', context)
