from .models import Airplains


def get_data(request, call_sign):
	data = dict()
	data['plain'] = Airplains.objects.get(call_sign=call_sign).pk
	data['latitude'] = request.data['latitude']
	data['longitude'] = request.data['longitude']
	data['altitude'] = request.data['altitude']
	data['heading'] = request.data['heading']

	return data