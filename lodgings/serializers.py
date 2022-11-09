from rest_framework import serializers
from lodgings.models import Lodging
from rooms.models import Room
from reviews.models import Review
from django.db.models import Avg


class LodgingSerializer(serializers.ModelSerializer):
    stars = serializers.SerializerMethodField()

    class Meta:
        model = Lodging
        fields = [
            'id',
            'name',
            'category',
            'stars',
            'description',
            'state',
            'city',
            'district',
            'street',
            'number',
            'complement',
            'cep',
            'email',
            'phone'
        ]
        read_only_fields = ['id', 'stars']

    def get_stars(self, obj):
        rooms = Room.objects.filter(lodging=obj)
        stars = Review.objects.filter(room__in=rooms).aggregate(Avg('stars'))
        return stars
