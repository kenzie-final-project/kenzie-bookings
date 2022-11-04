from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="review"
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        related_name="review"
    )

    title = models.CharField(max_length=255)
    review = models.TextField()
    stars = models. IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )