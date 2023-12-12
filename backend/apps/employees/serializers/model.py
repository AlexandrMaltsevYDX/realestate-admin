from rest_framework import serializers
from ..models.profile import Profile, MediaModel, ProfileImages


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class MediaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields = "__all__"


class ProfileImagesSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    media = MediaModelSerializer()

    class Meta:
        model = ProfileImages
        fields = "__all__"


class MediaListSerializer(serializers.Serializer):
    attachment = serializers.ListField(child=serializers.FileField())

    def create(self):
        attachments = self.validated_data.get("attachment", [])
        media_instances = [
            MediaModel(attachment=attachment) for attachment in attachments
        ]
        MediaModel.objects.bulk_create(media_instances)
        return media_instances
