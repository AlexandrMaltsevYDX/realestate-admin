from rest_framework import serializers
from apps.attributes import (
    models,
)


class WindowsOrientationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WindowsOrientation
        fields = "__all__"
