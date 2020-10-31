from django.db import models
from aiport_place.models import Airport_place


class Weather(models.Model):
    airport = models.ForeignKey(Airport_place, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    temperature = models.IntegerField()
    visibility = models.IntegerField()
    wind_speed = models.DecimalField(decimal_places=2, max_digits=5)
    wind_deg = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_update
