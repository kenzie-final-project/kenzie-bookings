from django.urls import path

from .views import ListBookingview, CreateBookingView, RetrieveBookingView, UpdateBookingView, DestroyBookingView

urlpatterns = [
    path("bookings/", ListBookingview.as_view()),
    path("lodgings/<int:lodging_id>/bookings", CreateBookingView.as_view()),
    path("bookings/<int:id>", RetrieveBookingView.as_view()),
    path("bookings/<int:id>", UpdateBookingView.as_view()),
    path("bookings/<int:id>", DestroyBookingView.as_view()),
]