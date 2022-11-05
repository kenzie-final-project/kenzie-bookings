from rest_framework import serializers
from lodgings.models import Lodging
from reviews.models import Review
from accounts.serializers import AccountSerializer
from django.db.models import Avg


class LodgingSerializer(serializers.ModelSerializer):
    stars = serializers.SerializerMethodField()
    host = AccountSerializer(read_only=True)

    class Meta:
        model = Lodging
        fields = [
            'id',
            'host',
            'category',
            'name',
            'stars',
            'description',
            'state',
            'city',
            'district',
            'street',
            'number',
            'complement',
            'cep'
        ]
        read_only_fields = ['id', 'stars']
        depth = 1

    def get_stars(self, obj):
        stars = Review.objects.aggregate(Avg('stars'))
        return stars
