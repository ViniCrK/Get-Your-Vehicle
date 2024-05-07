from django.contrib import admin
from vehicles import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ('id',)


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'brand', 'model',)
    list_per_page = 10
    ordering = ('-id',)
