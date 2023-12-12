from rest_framework import serializers
from apps.re_objects import models


class ReObjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReObject
        fields = "__all__"
