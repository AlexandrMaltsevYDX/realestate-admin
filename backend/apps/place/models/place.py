from django.db import models
from apps.place import models as _models


class Place(models.Model):
    country = models.ForeignKey(
        _models.Country,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Страна",
    )

    region = models.ForeignKey(
        _models.Region,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Регион",
    )

    city = models.ForeignKey(
        _models.City,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Город",
    )

    district = models.ForeignKey(
        _models.District,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Район",
    )

    street = models.ForeignKey(
        _models.Street,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Улица",
    )

    house = models.ForeignKey(
        _models.House,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Дом",
    )

    tag = models.ForeignKey(
        _models.Tag,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Тег",
    )

    flat = models.ForeignKey(
        _models.Flat,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Квартира",
    )

    coordinates = models.ForeignKey(
        _models.Coordinates,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Координаты",
    )

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house}, {self.tag}, {self.flat}"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
