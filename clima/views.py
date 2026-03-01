from rest_framework import viewsets
from .models import Location, WeatherHistory
from .serializers import LocationSerializer, WeatherHistorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from .services import WeatherService


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


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(detail=True, methods=['get'])
    def clima_actual(self, request, pk=None):
        location = self.get_object()
        datos_clima = WeatherService.obtener_y_guardar_clima(location)
        
        if datos_clima:
            return Response(datos_clima)
        return Response({"error": "No se pudo obtener el clima"}, status=500)
