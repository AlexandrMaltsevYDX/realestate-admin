# Generated by Django 4.2.5 on 2023-11-18 17:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0002_mediamodel_remove_profile_image_profileimages"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mediamodel",
            name="type",
        ),
    ]
