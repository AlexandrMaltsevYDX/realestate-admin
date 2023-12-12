from rest_framework import serializers
from apps.attributes import (
    models,
)


class LandCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LandCategory
        fields = "__all__"
