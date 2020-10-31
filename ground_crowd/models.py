from django.db import models
from aiport_place.models import Airport_place


class Groundcrew(models.Model):
	"""
	Maybe we have multiple airports so every airport can have different status
	"""

    airport = models.OneToOneField(Airport_place, on_delete=models.CASCADE)
    runway_clear = models.BooleanField(default=False)

    def __str__(self):
        return self.runway_clear