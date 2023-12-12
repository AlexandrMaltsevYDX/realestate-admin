from rest_framework import serializers
from apps.attributes import (
    models,
)


class OwnershipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ownership
        fields = "__all__"
