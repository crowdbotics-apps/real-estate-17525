from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Registered_agentViewSet

router = DefaultRouter()
router.register("registered_agent", Registered_agentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
