import pytest
from unittest.mock import patch
from clima.services import WeatherService
from clima.models import Location

@pytest.mark.django_db
@patch('clima.services.requests.get')
def test_weather_service_fetch_success(mock_get, db):
    # 1. Setup: Creamos una ubicación de prueba
    location = Location.objects.create(name="Test Field", latitude=10.0, longitude=-10.0)
    
    # 2. Mocking: Simulamos una respuesta exitosa de OpenWeather
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'main': {'temp': 25.5, 'humidity': 60, 'pressure': 1012},
        'weather': [{'description': 'clear sky', 'icon': '01d'}]
    }

    # 3. Execution: Llamamos al servicio
    result = WeatherService.fetch_and_save_weather(location)

    # 4. Assertions: Verificamos que se guardó en la DB y el resultado es correcto
    assert result['main']['temp'] == 25.5
    assert Location.objects.count() == 1
    # ¿Se creó el registro en WeatherHistory?
    from clima.models import WeatherHistory
    assert WeatherHistory.objects.count() == 1
    assert WeatherHistory.objects.first().description == 'clear sky'

