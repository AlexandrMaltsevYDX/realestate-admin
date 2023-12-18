from rest_framework.routers import DefaultRouter
from django.urls import include, path
from apps.place import (
    views,
)

router = DefaultRouter()


router.register(
    prefix=r"city",
    viewset=views.CityModelViewSet,
)

router.register(
    prefix=r"coordinates",
    viewset=views.CoordinatesModelViewSet,
)


router.register(
    prefix=r"country",
    viewset=views.CountryModelViewSet,
)

router.register(
    prefix=r"district",
    viewset=views.DistrictModelViewSet,
)


router.register(
    prefix=r"place",
    viewset=views.PlaceModelViewSet,
)

router.register(
    prefix=r"region",
    viewset=views.RegionModelViewSet,
)


router.register(
    prefix=r"street",
    viewset=views.StreetModelViewSet,
)


router.register(
    prefix=r"tag",
    viewset=views.TagModelViewSet,
)


urlpatterns = [
    path("place/", include(router.urls)),
]
