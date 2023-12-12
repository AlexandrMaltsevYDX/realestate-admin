from rest_framework import generics, views, viewsets, parsers, status

from drf_spectacular.utils import extend_schema


from apps.attributes import (
    models,
    serializers,
)


class EngineeringServicesModelViewSet(viewsets.ModelViewSet):
    queryset = models.EngineeringServices.objects.all()
    serializer_class = serializers.EngineeringServicesModelSerializer

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-engineering-services",),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-engineering-services",),
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Upload a file for YourModel.",
        tags=("attributes-engineering-services",),
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-engineering-services",),
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-engineering-services",),
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description="Custom description for the endpoint",
        tags=("attributes-engineering-services",),
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
