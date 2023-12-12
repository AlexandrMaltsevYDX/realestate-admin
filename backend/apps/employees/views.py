from drf_spectacular.utils import extend_schema
from rest_framework import views, viewsets, parsers, status
from rest_framework.response import Response
from rest_framework import views, status
from .models.profile import Profile, MediaModel, ProfileImages
from .serializers.model import (
    ProfileSerializer,
    ProfileImagesSerializer,
    MediaModelSerializer,
    MediaListSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @extend_schema(description="Custom description for the endpoint")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Upload a file for YourModel.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(description="Custom description for the endpoint")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class MediaView(views.APIView):
    parser_classes = (parsers.MultiPartParser, parsers.FileUploadParser)

    @extend_schema(
        request=MediaListSerializer,
        responses={200: None, 405: None},
        methods=["POST"],
        summary="Add new media files",
        description="Add new media files",
    )
    def post(self, request, *args, **kwargs):
        serializer = MediaListSerializer(data=request.data)
        if serializer.is_valid():
            test = serializer.create()
            print("==================>", test)
            # Assuming you want to create a MediaModel instance for each attachment

            return Response({"attachments": "attachments"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
