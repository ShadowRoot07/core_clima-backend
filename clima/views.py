from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Location, WeatherHistory
from .serializers import LocationSerializer, WeatherHistorySerializer
from .services import WeatherService

class LocationViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Locations (Gardens/Farms).
    Includes a custom action to fetch real-time weather.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(detail=True, methods=['get'], url_path='current-weather')
    def current_weather(self, request, pk=None):
        """
        Custom action: GET /api/locations/{id}/current-weather/
        Fetches data from OpenWeatherMap via WeatherService.
        """
        location = self.get_object()
        weather_data = WeatherService.fetch_and_save_weather(location)

        if weather_data:
            return Response(weather_data, status=status.HTTP_200_OK)
        
        return Response(
            {"error": "Could not fetch weather data from external API"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class WeatherHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only ViewSet for historical weather data.
    Records are created automatically when fetching current weather.
    """
    queryset = WeatherHistory.objects.all()
    serializer_class = WeatherHistorySerializer

