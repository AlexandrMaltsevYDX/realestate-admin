from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class MediaModel(models.Model):
    attachment = models.FileField(upload_to="files/")


class ProfileImages(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    media = models.ForeignKey("MediaModel", on_delete=models.CASCADE)
