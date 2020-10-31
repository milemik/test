from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = [
            'airport',
            'description',
            'temperature',
            'visibility',
            'wind_speed',
            'wind_deg',
            'last_update'
            ] 