from django.test import TestCase
import pytest
from .models import Airport_place


@pytest.mark.django_db()
def test_airport_place_model():
    airport_place = Airport_place.objects.all().count()

    assert airport_place == 0


@pytest.mark.django_db()
def test_create_airport_place_model():
    data = {
        "state": "Serbia",
        "town": "Belgrade",
        "runway_num": 1,
        "large_parkings": 5,
        "small_parkings": 10,
        "airport_name": "Nikola Tesla",
    }

    airport_place = Airport_place.objects.create(**data)

    assert Airport_place.objects.all().count() == 1
    assert airport_place.town == "Belgrade"
    assert airport_place.runway_num == 1
