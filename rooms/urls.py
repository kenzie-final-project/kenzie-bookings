from django.urls import path

from .views import RoomDetailView, RoomView

urlpatterns = [
    path("lodgings/<int:lodging_id>/rooms/", RoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", RoomDetailView.as_view()),
]
