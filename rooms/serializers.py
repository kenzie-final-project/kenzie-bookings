from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField(
        allow_null=True,
        allow_blank=True,
        min_value=0
    )
    cost = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        min_value=0.1
    )
    occupation = serializers.IntegerField(min_value=0)
    available = serializers.BooleanField(default=True)
    description = serializers.CharField(
        allow_null=True,
        allow_blank=True
    )

    created_at = serializers.DateTimeField(read_only=True, auto_now_add=True)
    updated_at = serializers.DateTimeField(read_only=True, auto_now=True)