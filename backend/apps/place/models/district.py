from django.db import models


class District(models.Model):
    name = models.CharField(max_length=255, verbose_name="Район")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
