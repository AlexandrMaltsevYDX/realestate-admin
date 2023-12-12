from django.db import models
from apps.attributes import models as attributes_models

from apps.employees.models.profile import MediaModel


# Create your models here.
class ReObject(models.Model):
    category = models.ForeignKey(
        attributes_models.Category,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категория объекта",
        help_text="Дом, Квартира, Участок",
    )
    type_house = models.ForeignKey(
        attributes_models.TypeHouse,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Тип объекта",
        help_text="Комерческая, ИЖС, Жилая",
    )
    number_of_storeys = models.PositiveIntegerField(
        verbose_name="Этажность",
        help_text="Количество этажей в здании",
        null=True,
    )
    floor = models.PositiveIntegerField(
        verbose_name="Этаж",
        help_text="Этаж в здании",
        null=True,
    )
    number_of_rooms = models.PositiveIntegerField(
        verbose_name="Количество комнат",
        help_text="Количество комнат в помещении",
        null=True,
    )
    total_area = models.FloatField(
        verbose_name="Общая площадь помещений",
        help_text="Общая площадь помещений",
        null=True,
    )
    living_area = models.FloatField(
        verbose_name="Жилая площадь",
        help_text="Жилая площадь в помещении",
        null=True,
    )
    kitchen_area = models.FloatField(
        verbose_name="Площадь кухни",
        help_text="Площадь кухни в помещении",
        null=True,
    )
    windows_orientation = models.ForeignKey(
        attributes_models.WindowsOrientation,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Ориентация окон",
        help_text="Запад, Север, Восток, и.т.д",
    )
    ownership = models.ForeignKey(
        attributes_models.Ownership,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Собственность",
        help_text="От собственника, Ипотека, и.т.д",
    )
    land_category = models.ForeignKey(
        attributes_models.LandCategory,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Категория земель",
        help_text="Комерческая",
    )
    land_area = models.FloatField(
        verbose_name="Площадь участка",
        help_text="Площадь участка",
        null=True,
    )

    relief_area = models.ForeignKey(
        attributes_models.ReliefArea,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Рельеф участка",
        help_text="Горы, Шморы",
    )
    fencing = models.ForeignKey(
        attributes_models.Fencing,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Ограждение",
        help_text="Горы, Шморы",
    )
    foundation = models.ForeignKey(
        attributes_models.Foundation,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Фундамент",
        help_text="Блоки, Лента, Плита",
    )
    wall_material = models.ForeignKey(
        attributes_models.WallMaterial,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Материал стен",
        help_text="Кирпич, Панель, Пеноблок",
    )
    buildings_on_site = models.TextField(
        max_length=1200,
        verbose_name="Здания на участке",
        help_text="Здания на участке",
        null=True,
    )
    buildings_of_vilages = models.PositiveIntegerField(
        verbose_name="Количество домов в поселке",
        help_text="Количество домов в поселке",
        null=True,
    )
    village_fences = models.ForeignKey(
        attributes_models.VillageFences,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Ограждение поселка",
        help_text="Да, нет",
    )

    object_description = models.ForeignKey(
        attributes_models.ObjectDescription,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Описание объекта",
        help_text="Текст в markdown",
    )

    class Meta:
        verbose_name = "Объекты недвижимости"
        verbose_name_plural = "Объекты недвижимости"


class ReObjectMedia(models.Model):
    re_object = models.ForeignKey(
        ReObject,
        on_delete=models.CASCADE,
    )
    media = models.ForeignKey(
        MediaModel,
        on_delete=models.CASCADE,
    )


class ReObjectEngineeringServices(models.Model):
    re_object = models.ForeignKey(
        ReObject,
        on_delete=models.CASCADE,
    )
    engineering_service = models.ForeignKey(
        attributes_models.EngineeringServices,
        on_delete=models.CASCADE,
    )
