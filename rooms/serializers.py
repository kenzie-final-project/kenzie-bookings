from rest_framework import serializers

from .models import Room
from lodgings.serializers import LodgingSerializer

class RoomSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    lodging = LodgingSerializer(read_only=True)
    
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1

    def create(self, validated_data):
        return Room.objects.create(**validated_data)
