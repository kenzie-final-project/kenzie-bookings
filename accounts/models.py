from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    is_host= models.BooleanField(default = False)
    REQUIRED_FIELDS = ["cpf"]
