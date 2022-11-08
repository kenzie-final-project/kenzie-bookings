from django.urls import path

from .views import ListBookingsView, CreateBookingView, RetrieveBookingView, UpdateBookingView, DestroyBookingView

urlpatterns = [
    path("bookings/", ListBookingsView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:room_id>/bookings/", CreateBookingView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:room_id>/bookings/<str:pk>", RetrieveBookingView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:room_id>/bookings/<str:pk>", UpdateBookingView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:room_id>/bookings/<str:pk>", DestroyBookingView.as_view()),
]
