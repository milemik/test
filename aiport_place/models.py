from django.db import models


class Airport_place(models.Model):
    state = models.CharField(max_length=100, null=False, blank=False)
    town = models.CharField(max_length=100, null=False, blank=False)
    runway_num = models.PositiveIntegerField(null=False, blank=False)
    large_parkings = models.PositiveIntegerField(null=False, blank=False)
    small_parkings = models.PositiveIntegerField(null=False, blank=False)
    airport_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.state}, {self.town}"
