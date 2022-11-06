from django.urls import path

from .views import ListRoomview, CreateRoomView, RetrieveRoomView, UpdateRoomView, DestroyRoomView

urlpatterns = [
    path("rooms/", ListRoomview.as_view()),
    path("lodgings/<int:lodging_id>/rooms", ListRoomview.as_view()),
    path("lodgings/<int:lodging_id>/rooms", CreateRoomView.as_view()),
    path("rooms/<int:id>", RetrieveRoomView.as_view()),
    path("rooms/<int:id>", UpdateRoomView.as_view()),
    path("rooms/<int:id>", DestroyRoomView.as_view()),
]
