from django.urls import path

from .views import GeneralRoomview, SpecificRoomView

urlpatterns = [
    path("rooms/", GeneralRoomview.as_view()),
    path("rooms/<id:int>", SpecificRoomView.as_view()),
]
