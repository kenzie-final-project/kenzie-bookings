from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name="add_full_name")

    def add_full_name(self, obj):
        return obj.full_name_method()

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('is_host') is not None:
            validated_data.pop('is_host')
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
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone",
            "is_host",
            "cpf",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ['full_name']

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


class AccountNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "username"
        ]