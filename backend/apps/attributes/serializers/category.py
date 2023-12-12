from rest_framework import serializers
from apps.attributes import (
    models,
)


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
