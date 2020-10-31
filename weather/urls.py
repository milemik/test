from django.urls import path
from .views import WeatherView


urlpatterns = [
    path('<str:call_sign>/weather/', WeatherView.as_view(), name="weather"),
]