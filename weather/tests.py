import pytest
import requests
from django.conf import settings

from .models import Weather
from aiport_place.models import Airport_place


@pytest.fixture
def airport():
    data = {
        "state": "Serbia",
        "town": "Belgrade",
        "runway_num": 1,
        "large_parkings": 5,
        "small_parkings": 10,
        "airport_name": "Nikola Tesla",
    }
    
    airport_place = Airport_place.objects.create(**data)
    return airport_place
    

@pytest.mark.django_db()
def test_weather_model():
    assert Weather.objects.all().count() == 0


@pytest.mark.django_db()
def test_create_weather_model(airport):

    airport_place = airport
    
    data = {
            "airport": airport_place, 
            "description": "broken clouds" ,
            "temperature": 25,
            "visibility": 10000,
            "wind_speed": 4.9,
            "wind_deg": 220,
        }
    weather = Weather.objects.create(**data)

    assert Weather.objects.all().count() == 1
    assert weather.wind_deg == 220


@pytest.mark.django_db()
def test_weather_api(airport):
    # http://api.openweathermap.org/data/2.5/weather?q=London,uk&callback=test&appid=1a1f91e2241e9056cf2dd4f9cf66e8da
    airport = airport
    
    city = airport.town

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}"
    print(url)

    r = requests.get(url)
    assert r.status_code == 200
    assert r.json()['name'] == city

    response_data = r.json()
    description = response_data['weather'][0]['description']
    temperature = response_data['main']['temp']
    visibility = response_data['visibility']
    wind_speed = response_data['wind']['speed']
    wind_deg = response_data['wind']['deg']

    Weather.objects.create(
        airport=airport,
        description=description,
        temperature=temperature,
        visibility=visibility,
        wind_speed=wind_speed,
        wind_deg=wind_deg,
    )

    assert Weather.objects.all().count() == 1

    