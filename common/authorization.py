from airplains.models import Airplains
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.permissions import BasePermission


class AirplainAuthorization(BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        print(request.headers)
        ssh_hub = request.headers.get("Authentication")
        
        airplain = Airplains.objects.filter(ssh_pub=ssh_hub[:255]).exists()
        return airplain