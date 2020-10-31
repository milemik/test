from django.conf import settings
import requests
from aiport_place.models import Airport_place
from .models import Weather
import json


def get_current_weather():

    all_airports = Airport_place.objects.all()
    for airport in all_airports:
        city = airport.city
    
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={settings.WEATHER_API_KEY}"

        r = requests.get(url)
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

