from rest_framework.permissions import BasePermission
from accounts.permissions import IsGuest, IsHostOrAdmin
from .models import Booking


class IsOwnerOrHosterOrAdmin(BasePermission):
    def has_permission(self, request, view):
        booking_id = view.kwargs['pk']
        booking = Booking.objects.get(id=booking_id)
        user = request.user

        return bool(
            user.is_authenticated and
            (
                user.is_superuser or
                (booking and booking.user == user) or
                (booking and booking.room.lodging.host == user and request.method == "GET")
            )
        )


class IsGuestOrHostOrAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return bool(
            user.is_authenticated and
            (
                user.is_superuser or
                (user.is_host is False) or
                (user.is_host is True and request.method == "GET")
            )
        )


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        booking_id = view.kwargs['pk']
        booking = Booking.objects.get(id=booking_id)
        user = request.user

        return bool(
            user.is_authenticated and
            (
                user.is_superuser or
                (booking and booking.user == user)
            )
        )
