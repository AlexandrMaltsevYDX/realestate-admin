from django.db import models


class Image(models.Model):
    attachment = models.FileField(upload_to="files/")

    # def __str__(self):
    # todo RE1-20

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
