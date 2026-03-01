import pytest
from clima.models import Location

@pytest.mark.django_db
def test_location_creation():
    # 1. Setup (Crear el objeto)
    location = Location.objects.create(
        name="Main Greenhouse",
        latitude=7.76,
        longitude=-72.22
    )
    
    # 2. Execution & Assertion (Verificar)
    assert location.name == "Main Greenhouse"
    assert str(location) == "Main Greenhouse (7.76, -72.22)"
    assert Location.objects.count() == 1

