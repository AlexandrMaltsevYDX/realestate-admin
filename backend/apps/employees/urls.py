from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import ProfileViewSet, MediaView


router = DefaultRouter()
router.register(prefix=r"emploeeys", viewset=ProfileViewSet)

urlpatterns = [
    path("media/", MediaView.as_view(), name="media"),
    path("", include(router.urls)),
]
