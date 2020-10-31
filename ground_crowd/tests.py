import pytest
from .models import Groundcrew
from weather.tests import airport

@pytest.mark.django_db()
def test_ground_crew_model():

    assert Groundcrew.objects.all().count() == 0


@pytest.mark.django_db()
def test_create_ground_crew(airport):
    airport = airport

    Groundcrew.objects.create(
        airport=airport,
        runway_clear=False,
        )

    assert Groundcrew.objects.all().count() == 1
    