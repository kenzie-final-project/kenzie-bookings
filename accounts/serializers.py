from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            password = validated_data.pop('password')
            self.instance.set_password(password)
        return super().update(instance, validated_data)

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

    def validate_username(self, username):
        user = Account.objects.filter(username=username).first()

        if user is None:
            return username
        elif user.id != self.context['request'].user.id:
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
