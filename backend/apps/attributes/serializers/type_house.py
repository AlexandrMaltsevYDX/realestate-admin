from rest_framework import serializers
from apps.attributes import (
    models,
)


class TypeHouseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeHouse
        fields = "__all__"
