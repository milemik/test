from django.test import TestCase
from django.urls import reverse
import pytest
from airplains.models import Airplains, Position
from rest_framework.test import RequestsClient, APIClient

from .factories import GroundCrewFactory, AirportPlaceFactory, PositionFactory


@pytest.fixture
def airplain_data():
    data = {
        "call_sign": "N243",
        "ssh_key": "qejddaiodjawijddij9890uu9390ud98jq38djq389dq389q98",
        "ssh_pub": "dkopokw0dkadka09kda0dksoidkoadk30d093ad9a90kd90akd9a0kd3a90dk9d0akd90k",
    }
    return data

@pytest.mark.django_db()
def test_airplains_model():

    assert Airplains.objects.all().count() == 0


@pytest.mark.django_db()
def test_create_airplain(airplain_data):
    data = airplain_data

    Airplains.objects.create(**data)

    assert Airplains.objects.all().count() == 1
    assert Airplains.objects.all().first().state == 0


@pytest.mark.django_db()
def test_plain_position():
    assert Position.objects.all().count() == 0


@pytest.mark.django_db()
def test_create_plain_position(airplain_data):
    plain_data = airplain_data
    plain = Airplains.objects.create(**plain_data)
    data = {
        "plain": plain,
        "latitude": 43.344253,
        "longitude": 23.343454,
        "altitude": 3400,
        "heading": 2000,

    }

    Position.objects.create(**data)

    assert Position.objects.all().count() == 1


@pytest.mark.django_db()
def test_position_view_api(airplain_data):
    plane = Airplains.objects.create(**airplain_data)
    airport = AirportPlaceFactory()
    gc = GroundCrewFactory(airport=airport)
    PositionFactory(plain=plane)

    client = RequestsClient()
    # client.credentials(HTTP_AUTHORIZATION=plane.ssh_pub)

    data = {
        "plain": plane.pk,
        "latitude": 2,
        "longitude": 2.0,
        "altitude": 2.0,
        "heading": 2,
        "position_time": 2,
    }

    url = f'http://localhost:8000/api/{plane.call_sign}/position/{plane.pk}'
    url = 'http://localhost:8000/api/N243/position/1/?plain=N243&latitude=0&longitude=1.0&altitude=1.0&heading=1&position_time=1'
    print(url)

    response = client.get(url, headers={'Authentication': plane.ssh_pub}, data=data)
    print(response)
    assert response.status_code == 405

    response = client.put(url, headers={'Authentication': plane.ssh_pub}, data=data)
    print(response.text)
    assert response.status_code == 200
