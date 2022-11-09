from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Booking
from .serializers import BookingSerializer
from .mixins import SerializerMixin, UserTypeMixin
from .permissions import IsOwnerOrHosterOrAdmin, IsGuestOrHostOrAdmin
from rooms.models import Room
from accounts.models import Account
from django.core.mail import send_mail
from django.conf import settings


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
        send_mail(
            subject = 'Obrigado por fazer sua reserva com a Kenzie Booking!',
            message = f'Olá {self.request.user.username}, Sua reserva foi feita com sucesso! \nO quarto {room.number} da hospedagem {room.lodging.name} está reservado para você de {self.request.data["checkin_date"]} até {self.request.data["checkout_date"]}! \nO valor total de sua reserva é de R${self.request.data["cost"]} \nAgradecemos novamente por usar o Kenzie Booking!',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [self.request.user.username],
            fail_silently = False
        )

        return serializer.save(room=room, user=self.request.user)


class BookingDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrHosterOrAdmin]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
