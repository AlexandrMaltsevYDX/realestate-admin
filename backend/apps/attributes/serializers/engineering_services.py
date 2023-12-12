from rest_framework import serializers
from apps.attributes import (
    models,
)


class EngineeringServicesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EngineeringServices
        fields = "__all__"
