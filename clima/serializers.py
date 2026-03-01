from rest_framework import serializers
from .models import Location, WeatherHistory

class WeatherHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherHistory
        fields = ['id', 'temperature', 'humidity', 'pressure', 'description', 'icon', 'recorded_at']

class LocationSerializer(serializers.ModelSerializer):
    history = WeatherHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude', 'history', 'created_at']

