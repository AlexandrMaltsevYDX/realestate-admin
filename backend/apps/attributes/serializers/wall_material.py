from rest_framework import serializers
from apps.attributes import (
    models,
)


class WallMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WallMaterial
        fields = "__all__"
