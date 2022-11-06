from django.urls import path

from .views import ListRoomView, CreateRoomView, RetrieveRoomView, UpdateRoomView, DestroyRoomView

urlpatterns = [
    path("lodgings/<int:lodging_id>/rooms/", ListRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/", CreateRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", RetrieveRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", UpdateRoomView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:pk>/", DestroyRoomView.as_view()),
]
