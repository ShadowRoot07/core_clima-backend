import requests
from django.conf import settings
from django.core.cache import cache
from .models import WeatherHistory

class WeatherService:
    API_KEY = settings.OPENWEATHER_API_KEY
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def fetch_and_save_weather(location_obj): # Renamed to English
        cache_key = f"weather_{location_obj.id}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        params = {
            'lat': location_obj.latitude,
            'lon': location_obj.longitude,
            'appid': WeatherService.API_KEY,
            'units': 'metric',
            'lang': 'en' # Changed to English
        }

        try:
            response = requests.get(WeatherService.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # Save to Database (History) using English fields
            WeatherHistory.objects.create(
                location=location_obj,
                temperature=data['main']['temp'],
                humidity=data['main']['humidity'],
                pressure=data['main']['pressure'],
                description=data['weather'][0]['description'],
                icon=data['weather'][0]['icon']
            )

            # Save to cache for 15 minutes
            cache.set(cache_key, data, 900)

            return data
        except Exception as e:
            print(f"Error: {e}")
            return None

