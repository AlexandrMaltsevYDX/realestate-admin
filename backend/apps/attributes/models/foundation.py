from django.db import models


class Foundation(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name="Тип фундамента",
        help_text="Тип фундамента",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Тип фундамента"
        verbose_name_plural = "Тип фундамента"
