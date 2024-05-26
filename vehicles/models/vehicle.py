from django.utils.text import slugify
from django.db import models
from .type import Type
from .brand import Brand
from .color import Color


class VehicleManager(models.Manager):
    def get_available(self):
        return self.filter(status='disponivel').order_by('type')


class Vehicle(models.Model):
    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    objects = VehicleManager()

    VEHICLE_STATUS = {
        'emrevisao': 'Em Revisão',
        'disponivel': 'Disponível',
        'indisponivel': 'Indisponível',
    }

    type = models.ForeignKey(
        Type, on_delete=models.SET_NULL, null=True, verbose_name='Tipo')
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, verbose_name='Marca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    image = models.ImageField(
        upload_to='images/%Y/%m/', null=True, verbose_name='Imagem')
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, null=True, verbose_name='Cor')
    manufacture_year = models.CharField(
        max_length=10, verbose_name='Ano de Fabricação')
    status = models.CharField(max_length=50, null=True,
                              choices=VEHICLE_STATUS, verbose_name='Status')
    price = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2, verbose_name='Preço')
    have_wheels = models.BooleanField(
        default=False, verbose_name='Possui Rodas')
    wheels_number = models.IntegerField(
        blank=True, null=True, verbose_name='Quantidade de Rodas')
    slug = models.SlugField(default='', unique=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.model)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.model}'
