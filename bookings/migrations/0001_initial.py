# Generated by Django 4.1.3 on 2022-11-05 17:52
# Generated by Django 4.1.3 on 2022-11-08 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rooms", "0002_room_lodging"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("checkin_date", models.DateField()),
                ("checkout_date", models.DateField()),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="rooms.room",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
