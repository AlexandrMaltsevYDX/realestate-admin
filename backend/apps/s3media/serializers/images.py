from rest_framework import serializers
from apps.s3media import models


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = "__all__"


class ImageListSerializer(serializers.Serializer):
    attachment = serializers.ListField(child=serializers.FileField())

    def create(self):
        attachments = self.validated_data.get("attachment", [])
        media_instances = [
            models.Image(attachment=attachment) for attachment in attachments
        ]
        models.Image.objects.bulk_create(media_instances)
        return media_instances
