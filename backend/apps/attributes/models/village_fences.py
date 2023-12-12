from django.db import models


class VillageFences(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name="Ограждения в поселке",
        help_text="Ограждения в поселке",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Ограждения в поселке"
        verbose_name_plural = "Ограждения в поселке"
