# Generated by Django 4.2.5 on 2023-12-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
        ('re_objects', '0007_reobject_object_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='reobject',
            name='place',
            field=models.ForeignKey(help_text='Укажите месторасположение объекта', null=True, on_delete=django.db.models.deletion.CASCADE, to='place.place', verbose_name='Адресс'),
        ),
    ]
