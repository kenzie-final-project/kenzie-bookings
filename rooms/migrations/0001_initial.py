from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("lodgings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.PositiveIntegerField(blank=True, null=True)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=20)),
                ("occupation", models.PositiveIntegerField()),
                ("available", models.BooleanField(default=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "lodging",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lodgings.lodging",
                    ),
                ),
            ],
        ),
    ]
