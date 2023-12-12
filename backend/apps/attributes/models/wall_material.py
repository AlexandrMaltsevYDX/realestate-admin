from django.db import models


class WallMaterial(models.Model):
    value = models.CharField(
        max_length=50,
        verbose_name="Материал стен",
        help_text="Материал стен",
    )

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Материал стен"
        verbose_name_plural = "Материал стен"
