from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vehicle


class ListVehiclesView(ListView):
    model = Vehicle
    template_name = 'vehicles/list_vehicles.html'
    context_object_name = 'vehicles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'site_title': 'Veículos'
        })

        return context


class DetailVehicleView(DetailView):
    ...
