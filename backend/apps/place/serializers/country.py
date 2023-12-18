from rest_framework import serializers
from apps.place import models


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"
