from rest_framework import generics, views, viewsets, parsers, status

from drf_spectacular.utils import extend_schema


from apps.attributes import (
    models,
    serializers,
)


class OwnershipModelViewSet(viewsets.ModelViewSet):
    queryset = models.Ownership.objects.all()
    serializer_class = serializers.OwnershipModelSerializer

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-ownership",),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-ownership",),
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Upload a file for YourModel.",
        tags=("attributes-ownership",),
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-ownership",),
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-ownership",),
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-ownership",),
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
