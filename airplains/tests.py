from django.test import TestCase
from django.urls import reverse
import pytest
from .models import Airplains, Position
from rest_framework.test import RequestsClient


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
    client = RequestsClient()

    url = 'http://localhost:8000/api/NC9574/intent/'

    response = client.get(url, headers={'Authentication': plane.ssh_pub})
    assert response.status_code == 405

    response = client.put(url, headers={'Authentication': plane.ssh_pub})
    assert response.status_code == 200
    