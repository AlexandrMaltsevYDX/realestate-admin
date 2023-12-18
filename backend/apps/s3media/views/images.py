from drf_spectacular.utils import extend_schema
from rest_framework import views, parsers, status
from rest_framework.response import Response
from rest_framework import views, status
from apps.s3media import (
    serializers,
)


class ImageView(views.APIView):
    parser_classes = (parsers.MultiPartParser, parsers.FileUploadParser)

    @extend_schema(
        request=serializers.ImageListSerializer,
        responses={200: None, 405: None},
        methods=["POST"],
        summary="Add new media files",
        description="Add new media files",
    )
    def post(self, request, *args, **kwargs):
        serializer = serializers.ImageListSerializer(data=request.data)
        if serializer.is_valid():
            test = serializer.create()
            print("==================>", test)
            # Assuming you want to create a MediaModel instance for each attachment
            return Response({"attachments": "attachments"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
