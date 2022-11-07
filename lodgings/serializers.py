from rest_framework import serializers
from lodgings.models import Lodging
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
        stars = Review.objects.aggregate(Avg('stars'))
        return stars
