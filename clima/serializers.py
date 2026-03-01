from rest_framework import serializers
from .models import Location, WeatherHistory

class WeatherHistorySerializer(serializers.ModelSerializer):
    # Campo calculado dinámicamente
    status = serializers.SerializerMethodField()

    class Meta:
        model = WeatherHistory
        fields = ['id', 'temperature', 'humidity', 'pressure', 'description', 'icon', 'recorded_at', 'status']

    def get_status(self, obj):
        if obj.temperature > 30:
            return "Extreme Heat - Check Irrigation"
        elif obj.temperature < 10:
            return "Cold Alert - Protect Sensitive Plants"
        return "Optimal"


class LocationSerializer(serializers.ModelSerializer):
    history = WeatherHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude', 'history', 'created_at']
