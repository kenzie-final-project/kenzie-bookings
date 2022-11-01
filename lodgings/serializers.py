from rest_framework import serializers
from .models import Lodging
# from accounts.models import Account


class LodgingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lodging