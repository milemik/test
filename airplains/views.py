from .models import Position, Airplains
from ground_crowd.models import Groundcrew
from common.authorization import AirplainAuthorization
from .serializers import PositionSerializer, AirplainsSerializer
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import status


class PositionView(generics.GenericAPIView, mixins.UpdateModelMixin):

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (AirplainAuthorization,)
    

    def put(self, request, call_sign, pk=None):
        if Airplains.objects.filter(call_sign=call_sign).exists():
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_406_NOT_ACCEPTABLE)


class PlainChangeStatus(generics.GenericAPIView, mixins.UpdateModelMixin):

    queryset = Airplains
    serializer_class = AirplainsSerializer
    permission_classes = (AirplainAuthorization,)

    def put(self, request, call_sign):
        """
        For simplicity check only for Belgrade airport status
        """
        if Airplains.objects.filter(call_sign=call_sign).exists() and Groundcrew.objects.filter(runway_clear=True):
            plain = Airplains.objects.get(call_sign=call_sign)
            plain.state=request.data['state']
            plain.save()
            return Response("OK")
        else:
            return Response({"Not possible now": 0})
