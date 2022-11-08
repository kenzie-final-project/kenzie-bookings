from rest_framework import serializers
from reviews.models import Review
from django.db.models import Avg

from .models import Room
from lodgings.serializers import LodgingSerializer


class RoomSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # lodging = LodgingSerializer(read_only=True)
    stars = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['id', 'stars']

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

    def get_stars(self, obj):
        stars = Review.objects.filter(room=obj).aggregate(Avg('stars'))
        return stars
