from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13, unique=True)

    def set_password(self, raw_password):
        super().set_password(raw_password)

    def __str__(self):
        return self.username
