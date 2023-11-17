from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import aiViewSet

router = DefaultRouter()

router.register(r'ai', aiViewSet)

urlpatterns = [
    path('', include(router.urls))
]
