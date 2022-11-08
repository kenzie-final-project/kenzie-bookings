from rest_framework import serializers

from accounts.serializers import AccountSerializer
from rooms.serializers import RoomSerializer
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class SpecificBookingSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = [
            'id',
            'checkin_date',
            'checkout_date',
            'cost',
        ]
