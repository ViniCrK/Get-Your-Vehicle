from django.db import models


class Color(models.Model):
    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'
