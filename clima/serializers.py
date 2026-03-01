from rest_framework import serializers
from .models import Location, WeatherHistory

class WeatherHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherHistory
        fields = ['id', 'temperatura', 'humedad', 'presion', 'descripcion', 'icono', 'fecha_registro']

class LocationSerializer(serializers.ModelSerializer):
    # Esto permite que al pedir una ubicación, opcionalmente veas su historial
    history = WeatherHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'nombre', 'latitud', 'longitud', 'history', 'fecha_creacion']

