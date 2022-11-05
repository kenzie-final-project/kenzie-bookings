from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "name",
            "phone",
            "is_host",
            "is_superuser",
            "cpf",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["is_host", "cpf"]

    def validate_username(self, username):
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already exists")

        return username
