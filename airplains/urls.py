from django.urls import path
from .views import PositionView, PlainChangeStatus


urlpatterns = [
    path('<str:call_sign>/position/<int:pk>/', PositionView.as_view(), name="position"),
    path('<str:call_sign>/intent/', PlainChangeStatus.as_view(), name="intent"),
]
