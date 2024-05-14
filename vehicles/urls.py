from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('', views.ListVehiclesView.as_view(), name='list'),
    path('<slug:slug>/', views.DetailVehicleView.as_view(), name='detail'),
]
