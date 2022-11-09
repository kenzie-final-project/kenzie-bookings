from django.db import models
from django.core.validators import MinValueValidator


class LodgingCategories(models.TextChoices):
    HOTEL = 'Hotel'
    RESORT = 'Resort'
    POUSADA = 'Pousada'


class Lodging(models.Model):
    host = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="lodging"
    )
    category = models.CharField(
        max_length=20,
        choices=LodgingCategories.choices,
        default=LodgingCategories.HOTEL
    )
    description = models.TextField()
    name = models.CharField(max_length=127)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=127)
    district = models.CharField(max_length=127)
    street = models.CharField(max_length=127)
    number = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    complement = models.CharField(max_length=30, blank=True)
    cep = models.CharField(max_length=8)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
