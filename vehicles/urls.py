from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('', views.ListVehicles.as_view(), name='list'),
]
