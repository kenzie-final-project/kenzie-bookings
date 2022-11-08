from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .models import Booking
from ..lodgings.models import Lodging
from .serializers import BookingSerializer
from .mixins import SerializerMixin
from .permissions import IsOwnerOrAdmin

    
class ListBookingsView(SerializerMixin, ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class CreateBookingView(SerializerMixin, CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        return serializer.save(lodging_id=self.kwargs.get('lodging_id'))

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
