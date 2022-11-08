from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Booking
from .serializers import BookingSerializer
from .mixins import SerializerMixin
from .permissions import IsOwnerOrAdmin, IsGuest
from rooms.models import Room


class ListBookingsView(SerializerMixin, ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CreateBookingView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGuest]
    queryset = Booking.objects
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        room_id = self.kwargs.get('room_id')
        user = self.request.user
        print("TEST", room_id, user.id)

        return serializer.save(room_id=room_id, user=user)


class RetrieveBookingView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UpdateBookingView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class DestroyBookingView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
