from rest_framework import serializers

from accounts.serializers import AccountSerializer
from rooms.serializers import RoomSerializer
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """ user = AccountSerializer(write_only=True)
    room = RoomSerializer(write_only=True) """

    class Meta:
        model = Booking
        fields = ['id', 'checkin_date', 'checkout_date', 'cost']
        read_only_fields = ['id']


class SpecificBookingSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = [
            'id',
            'checkin_date',
            'checkout_date',
            'cost',
        ]
        read_only_fields = ['cost']
