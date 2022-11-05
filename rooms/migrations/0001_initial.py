from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
            ],
        ),
    ]
