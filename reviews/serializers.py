from rest_framework import serializers
from reviews.models import Review
from accounts.serializers import AccountSerializer
from rooms.serializers import RoomSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = AccountSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'room', 'title', 'review', 'stars']
        read_only_fields = ['id']
        depth= 1
