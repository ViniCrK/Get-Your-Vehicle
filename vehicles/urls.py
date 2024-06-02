from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('', views.ListVehiclesView.as_view(), name='list'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('<slug:slug>/', views.DetailVehicleView.as_view(), name='detail'),
    path('<slug:slug>/rent/', views.RentVehicleView.as_view(), name='rent'),
]
