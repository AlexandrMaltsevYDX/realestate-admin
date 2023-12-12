from django.db import models


class TypeHouse(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип объекта"
        verbose_name_plural = "Тип объекта"
