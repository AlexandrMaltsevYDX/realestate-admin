from rest_framework import serializers
from apps.attributes import (
    models,
)


class FoundationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Foundation
        fields = "__all__"
