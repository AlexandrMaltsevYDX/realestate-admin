from django.db import models


class ReliefArea(models.Model):
    value = models.CharField(
        verbose_name="Рельеф участка",
        help_text="Рельеф участка",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Рельеф участка"
        verbose_name_plural = "Рельеф участка"
