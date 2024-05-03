from django.db import models
from .type import Type
from .brand import Brand
from .color import Color


class Vehicle(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=50)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    manufacture_year = models.CharField(max_length=10)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    wheels_number = models.IntegerField(blank=True, null=True)
