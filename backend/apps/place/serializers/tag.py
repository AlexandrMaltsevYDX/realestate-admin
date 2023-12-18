from rest_framework import serializers
from apps.place import models


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"
