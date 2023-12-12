from rest_framework.routers import DefaultRouter
from django.urls import include, path
from apps.re_objects import (
    views,
)

router = DefaultRouter()

router.register(prefix=r"unit", viewset=views.ReObjectModel)

urlpatterns = [
    path("re_objects/", include(router.urls)),
]
