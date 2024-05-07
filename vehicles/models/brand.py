from django.db import models


class Brand(models.Model):
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'
