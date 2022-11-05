from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name="add_full_name")
    def add_full_name(self,obj):
        return obj.full_name_method()
    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "first_name"
            "last_name"
            "email",
            "phone",
            "is_host",
            "cpf",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, username):
        if Account.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already exists")

        return username


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "email",
            "phone"
        ]
