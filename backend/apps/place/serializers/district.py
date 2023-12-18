from rest_framework import serializers
from apps.place import models


class DistrictModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = "__all__"
