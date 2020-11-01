from factory.django import DjangoModelFactory
import factory

from aiport_place.models import Airport_place
from airplains.models import Airplains, Position
from ground_crowd.models import Groundcrew


class AirportPlaceFactory(DjangoModelFactory):

	state = "Serbia"
	town = "Belgrade"
	runway_num = 1
	large_parkings = 5
	small_parkings = 10
	airport_name = "Nikola Tesla"

	class Meta:
		model = Airport_place


class AirplainsFactory(DjangoModelFactory):
	call_sign = 'SING123'
	ssh_key = 'djiao3e930dk90adka30dkad'
	ssh_pub = 'dk9093rd0j390d3jd0ad9dj0dja8d0j20j92a0daj2d9a2jda029dja29dj2a'
	state = 0
	plain_type = 0

	class Meta:
		model = Airplains


class GroundCrewFactory(DjangoModelFactory):

	airport = factory.SubFactory(AirplainsFactory)
	runway_clear = False

	class Meta:
		model = Groundcrew


class PositionFactory(DjangoModelFactory):
	plain = factory.SubFactory(AirplainsFactory)
	latitude = 0
	longitude = 1.0
	altitude = 1.0
	heading = 1
	position_time = 1

	class Meta:
		model = Position
