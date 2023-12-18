from rest_framework import serializers
from apps.place import models


class PlaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = "__all__"
