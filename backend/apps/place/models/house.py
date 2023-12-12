from django.db import models


class House(models.Model):
    name = models.PositiveIntegerField(
        verbose_name="Дом",
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
