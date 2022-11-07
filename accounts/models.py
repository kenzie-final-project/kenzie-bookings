from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=11)
    is_host = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["cpf"]
    
    def full_name_method(self):
        return f'{self.first_name} {self.last_name}'