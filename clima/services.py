import requests
from django.conf import settings

class WeatherService:
    # Mañana configuraremos la API_KEY en los settings
    API_KEY = "TU_LLAVE_AQUI_O_EN_ENV"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def obtener_clima_actual(lat, lon):
        params = {
            'lat': lat,
            'lon': lon,
            'appid': WeatherService.API_KEY,
            'units': 'metric', # Para que nos de Celsius directamente
            'lang': 'es'       # Para que la descripción sea en español
        }
        
        try:
            response = requests.get(WeatherService.BASE_URL, params=params)
            response.raise_for_status() # Lanza error si la API falla
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error llamando a OpenWeather: {e}")
            return None

