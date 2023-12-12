from rest_framework import serializers
from apps.attributes import (
    models,
)


class VillageFencesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VillageFences
        fields = "__all__"
