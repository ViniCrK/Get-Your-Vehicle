from django.db import models


class Type(models.Model):
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'
