from django.db.models import Q

from .models import Groundcrew
from airplains.models import Airplains
from aiport_place.models import Airport_place

def update_ground_crew_belgrade():
    """
        For simplicity of the task I will create a cron job
        for checking only belgrade runway availability
    """
    bg_airport = Airport_place.objects.get(town="Belgrade")

    if bg_airport and Airplains.objects.filter(Q(status=1) | Q(status=4)).exists():
        Groundcrew.objects.get_or_create(airport=bg_airport, runway_clear=False)
    else:
        Groundcrew.objects.get_or_create(airport=bg_airport, runway_clear=True)
    

