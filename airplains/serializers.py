from .models import Position, Airplains
from rest_framework import serializers



class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = (
            'plain',
            'latitude',
            'longitude',
            'altitude',
            'heading',
            )


class AirplainsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplains
        fields = ('state',)
