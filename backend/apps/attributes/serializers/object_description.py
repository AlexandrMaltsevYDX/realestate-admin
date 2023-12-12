from rest_framework import serializers
from apps.attributes import (
    models,
)


class ObjectDescriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectDescription
        fields = "__all__"
