from django.db import models


class Room(models.Model):
    # Nulável, pois o tipo de identificação do estabelecimento seja outro (letras, apelidos...)
    number = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    cost = models.DecimalField(
        max_digits=20,
        decimal_places=2
    )
    occupation = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    lodging = models.ForeignKey(
        "lodgings.Lodging",
        on_delete=models.CASCADE
    )
