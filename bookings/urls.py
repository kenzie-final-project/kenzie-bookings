from django.urls import path

from .views import ListBookingsView, BookingView, BookingDetailView
# , UpdateBookingView, DestroyBookingView

urlpatterns = [
    path("bookings/", ListBookingsView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:room_id>/bookings/", BookingView.as_view()),
    path("lodgings/<int:lodging_id>/rooms/<int:room_id>/bookings/<pk>/", BookingDetailView.as_view()),
]
