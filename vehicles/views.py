from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.db.models import Q
from .models import Vehicle


class ListVehiclesView(LoginRequiredMixin, ListView):
    model = Vehicle
    paginate_by = 6
    template_name = 'vehicles/list.html'
    context_object_name = 'vehicles'
    queryset = Vehicle.objects.get_available()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'site_title': 'Veículos'
        })

        return context


class SearchListView(ListVehiclesView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._search_value = ''

    def setup(self, request, *args, **kwargs):
        self._search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        search_value = self._search_value
        return super().get_queryset().filter(
            Q(model__icontains=search_value) |
            Q(brand__name__icontains=search_value)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_value = self._search_value

        context.update({
            'site_title': f'Busca: {search_value[:30]}',
            'search_value': search_value,
        })

        return context

    def get(self, request, *args, **kwargs):
        if self._search_value == '':
            return redirect('vehicles:list')

        return super().get(request, *args, **kwargs)


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


class RentVehicleView(DetailView):
    def post(self, request, *args, **kwargs):
        vehicle = Vehicle.objects.get(slug=kwargs['slug'])

        vehicle.status = 'locado'
        vehicle.save()

        return redirect('vehicles:list')
