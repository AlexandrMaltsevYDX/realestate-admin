from django.db import models


class WindowsOrientation(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name="Ориентация окон",
        help_text="Ориентация окон",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Ориентация окон"
        verbose_name_plural = "Ориентация окон"
