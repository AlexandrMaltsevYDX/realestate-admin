from rest_framework import serializers
from apps.place import models


class StreetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Street
        fields = "__all__"
