from django.urls import path
from .views import PositionView, PlainChangeStatus, CreatePosition


urlpatterns = [
    path('<str:call_sign>/position/<int:pk>/', PositionView.as_view(), name="position"),
    path('<str:call_sign>/intent/<int:pk>/', PlainChangeStatus.as_view(), name="intent"),
    path('<str:call_sign>/create_position/', CreatePosition.as_view(), name="create-position")
]
