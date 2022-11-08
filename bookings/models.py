from django.db import models
import uuid


class Booking(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.OneToOneField(
        'accounts.Account',
        on_delete=models.CASCADE
    )

    room = models.OneToOneField(
        'rooms.Room',
        on_delete=models.CASCADE
    )
