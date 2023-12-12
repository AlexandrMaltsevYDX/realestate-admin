from django.db import models


class EngineeringServices(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name="Инженерные сети",
        help_text="Наличие инженерных сетей",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Инженерные сети"
        verbose_name_plural = "Инженерные сети"
