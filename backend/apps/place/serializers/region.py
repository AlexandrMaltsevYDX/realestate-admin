from rest_framework import serializers
from apps.place import models


class RegionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = "__all__"
