from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, WeatherHistoryViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'history', WeatherHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

