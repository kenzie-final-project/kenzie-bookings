from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Booking
from .serializers import BookingSerializer
from .mixins import SerializerMixin, UserTypeMixin
from .permissions import IsOwnerOrHosterOrAdmin, IsGuestOrHostOrAdmin
from rooms.models import Room
from accounts.models import Account


class ListBookingsView(UserTypeMixin, ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGuestOrHostOrAdmin]
    queryset = Booking.objects.all()
    serializer_map = {
        "admin": BookingSerializer,
        "host": BookingSerializer,
        "guest": BookingSerializer,
    }


class BookingView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsGuestOrHostOrAdmin]
    queryset = Booking.objects
    serializer_class = BookingSerializer

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return self.queryset.filter(room_id=room_id)

    def perform_create(self, serializer):
        room_id = self.kwargs.get('room_id')
        room = Room.objects.get(id=room_id)
        room.available = False
        room.save()
        return serializer.save(room=room, user=self.request.user)


class BookingDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrHosterOrAdmin]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
