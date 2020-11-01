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

    def update(self, instance, validated_data):
        instance.plain = validated_data.get('plain')
        instance.latitude = validated_data.get('latitude')
        instance.longitude = validated_data.get('longitude')
        instance.altitude = validated_data.get('altitude')
        instance.heading = validated_data.get('heading')
        return instance


class AirplainsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplains
        fields = ('state',)

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state')
        return instance
