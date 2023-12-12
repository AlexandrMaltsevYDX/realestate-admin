from django.db import models


class LandCategory(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name="Категория земли",
        help_text="Категория земли",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Категория земель"
        verbose_name_plural = "Категория земель"
