from django.db import models


class Flat(models.Model):
    name = models.PositiveIntegerField(verbose_name="Квартира", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
