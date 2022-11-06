from django.urls import path

from .views import ListLodgingRoomsView, ListRoomView, CreateRoomView, RetrieveRoomView, UpdateRoomView, DestroyRoomView

urlpatterns = [
    path("rooms/", ListRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms", ListLodgingRoomsView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/", CreateRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", RetrieveRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", UpdateRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", DestroyRoomView.as_view()),
]
