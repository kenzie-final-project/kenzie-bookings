from rest_framework import serializers
from reviews.models import Review
from accounts.serializers import AccountNameSerializer
from rooms.serializers import RoomSerializer


class ReviewSerializer(serializers.ModelSerializer):
    # user = AccountNameSerializer(read_only=True)
    # room = RoomSerializer(read_only=True)
    username = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'username', 'title', 'review', 'stars']
        read_only_fields = ['id']

    def get_username(self, obj):
        user = obj.user
        return user.username
