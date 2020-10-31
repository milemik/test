from django.db import models


class Airplains(models.Model):

    STATES = (
        (0, "PARKED"),
        (1, "TAKE-OFF"),
        (2, "AIRBORNE"),
        (3, "APPROACH"),
        (4, "LANDED")
    )

    TYPE = (
        (0, "AIRLINER"),
        (1, "PRIVATE"),
    )

    call_sign = models.CharField(max_length=20, null=False, blank=False)
    ssh_key = models.CharField(max_length=255, null=False, blank=False)
    ssh_pub = models.CharField(max_length=255, null=False, blank=False)
    state = models.PositiveIntegerField(choices=STATES, default=0)
    plain_type = models.PositiveIntegerField(choices=TYPE, default=0)


    def __str__(self):
        return self.call_sign


class Position(models.Model):
    plain = models.ForeignKey(Airplains, on_delete=models.CASCADE)
    latitude = models.DecimalField(decimal_places=14, max_digits=20)
    longitude = models.DecimalField(decimal_places=14, max_digits=20)
    altitude = models.IntegerField()
    heading = models.IntegerField()
    position_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plain.call_sign

    class Meta:
        ordering = ['-position_time']