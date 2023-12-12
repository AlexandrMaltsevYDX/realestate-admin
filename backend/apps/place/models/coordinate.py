from django.db import models


class Coordinates(models.Model):
    ydx_latitude = models.FloatField(null=True, verbose_name="Широта(Яндекс)")
    ydx_longitude = models.FloatField(null=True, verbose_name="Долгота(Яндекс)")

    def __str__(self):
        return f"{self.ydx_latitude}  ,  {self.ydx_longitude}"

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"
