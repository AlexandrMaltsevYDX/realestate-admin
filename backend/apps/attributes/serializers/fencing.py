from rest_framework import serializers
from apps.attributes import (
    models,
)


class FencingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fencing
        fields = "__all__"
