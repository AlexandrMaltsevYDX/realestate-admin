from django.db import models


class ObjectDescription(models.Model):
    value = models.TextField(
        max_length=2500,
        verbose_name="Описание объекта",
        help_text="Используйте маркдаун",
    )

    def __str__(self):
        return self.value[:25]

    class Meta:
        verbose_name = "Описание объекта"
        verbose_name_plural = "Описание объекта"
