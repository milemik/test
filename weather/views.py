from rest_framework.response import Response
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework import generics, mixins

from airplains.models import Airplains

class WeatherView(generics.GenericAPIView, mixins.RetrieveModelMixin):

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get(self, request, call_sign):
        if Airplains.objects.filter(call_sign=call_sign).exists():
            serializer = WeatherSerializer(self.queryset.first())
            return Response(serializer.data)
        else:
            return Response("WRONG!")
