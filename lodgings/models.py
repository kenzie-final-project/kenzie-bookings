from django.db import models
from django.core.validators import MinValueValidator


class LodgingsCategories(models.TextChoices):
    HOTEL = 'Hotel'
    RESORT = 'Resort'
    POUSADA = 'Pousada'


class Lodgings(models.Model):
    """ host = models.ForeignKey(
        "accounts.User", 
        on_delete=models.CASCADE,
        related_name="lodging"
    ) """
    category = models.CharField(
        max_length=20,
        choices=LodgingsCategories.choices,
        default=LodgingsCategories.HOTEL
    )
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
    complement = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)