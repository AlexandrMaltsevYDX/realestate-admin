from rest_framework import serializers
from apps.place import models


class CoordinatesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coordinates
        fields = "__all__"
