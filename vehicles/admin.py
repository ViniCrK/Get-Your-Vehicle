from django.contrib import admin
from vehicles import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('name',)


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('name',)


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('name',)


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'type',)
    list_display_links = ('model',)
    list_filter = ('type', 'status', 'brand',
                   'have_wheels', 'manufacture_year',)
    list_per_page = 10
    ordering = ('model',)
    search_fields = ('model',)
