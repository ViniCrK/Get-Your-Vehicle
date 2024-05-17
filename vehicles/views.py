from django.views.generic import ListView, DetailView
from .models import Vehicle


class ListVehiclesView(ListView):
    model = Vehicle
    template_name = 'vehicles/list.html'
    context_object_name = 'vehicles'
    queryset = Vehicle.objects.filter(status='D')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'site_title': 'Veículos'
        })

        return context


class DetailVehicleView(DetailView):
    model = Vehicle
    template_name = 'vehicles/detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        vehicle = context[self.context_object_name]

        context.update({
            'site_title': vehicle.model
        })

        return context
