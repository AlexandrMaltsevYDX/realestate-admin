from rest_framework.routers import DefaultRouter
from django.urls import include, path
from apps.attributes import (
    views,
)

router = DefaultRouter()

router.register(
    prefix=r"category",
    viewset=views.CategoryModelViewSet,
)
router.register(
    prefix=r"engineering-services",
    viewset=views.EngineeringServicesModelViewSet,
)
router.register(
    prefix=r"fencing",
    viewset=views.FencingModelViewSet,
)
router.register(
    prefix=r"foundation",
    viewset=views.FoundationModelViewSet,
)
router.register(
    prefix=r"land-category",
    viewset=views.LandCategoryModelViewSet,
)
router.register(
    prefix=r"ownership",
    viewset=views.OwnershipModelViewSet,
)
router.register(
    prefix=r"relief",
    viewset=views.ReliefAreaModelViewSet,
)
router.register(
    prefix=r"type-house",
    viewset=views.TypeHouseModelViewSet,
)
router.register(
    prefix=r"village-fences",
    viewset=views.VillageFencesModelViewSet,
)
router.register(
    prefix=r"windows-orientation",
    viewset=views.WindowsOrientationModelViewSet,
)
router.register(
    prefix=r"wall-material",
    viewset=views.WallMaterialModelViewSet,
)
router.register(
    prefix=r"object-description",
    viewset=views.ObjectDescriptionModelViewSet,
)

urlpatterns = [
    path("attributes/", include(router.urls)),
]
