from rest_framework import serializers
from apps.place import models


class CityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"
