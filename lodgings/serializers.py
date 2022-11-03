from rest_framework import serializers
from lodgings.models import Lodging
# from accounts.models import Account


class LodgingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lodging
        fields = '__all__'
        read_only_fields = ['id']