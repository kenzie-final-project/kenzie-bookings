from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True, auto_now_add=True)
    updated_at = serializers.DateTimeField(read_only=True, auto_now=True)

    class Meta:
        model = Room
        fields = '__all__'
