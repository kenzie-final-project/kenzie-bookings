from rest_framework import serializers

from accounts.serializers import AccountSerializer
from rooms.serializers import RoomSerializer
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """ user = AccountSerializer(write_only=True)
    room = RoomSerializer(write_only=True) """
    # cost = serializers.SerializerMethodField(method_name="add_cost")

    class Meta:
        model = Booking
        fields = ['id', 'checkin_date', 'checkout_date', 'cost']
        read_only_fields = ['id', 'cost']

    def create(self, validated_data):
        days = (validated_data["checkout_date"] - validated_data["checkin_date"]).days
        validated_data["cost"] = validated_data["room"].cost * days
        return super().create(validated_data)

    def update(self, instance, validated_data):

        checkin = validated_data.get("checkin_date")
        if checkin is None:
            checkin = instance.checkin_date

        checkout = validated_data.get("checkout_date")
        if checkout is None:
            checkout = instance.checkout_date

        validated_data["cost"] = instance.room.cost * (checkout - checkin).days
        return super().update(instance, validated_data)


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
