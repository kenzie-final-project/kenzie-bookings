from rest_framework import serializers

from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        return Room.objects.create(**validated_data)