from rest_framework import serializers
from apps.attributes import (
    models,
)


class ReliefAreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReliefArea
        fields = "__all__"
