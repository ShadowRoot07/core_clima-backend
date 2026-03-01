from rest_framework import viewsets
from .models import Location, WeatherHistory
from .serializers import LocationSerializer, WeatherHistorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_serializer = LocationSerializer

class WeatherHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Solo lectura porque el historial se creará vía API externa, 
    no manualmente desde el frontend de React.
    """
    queryset = WeatherHistory.objects.all()
    serializer_class = WeatherHistorySerializer

