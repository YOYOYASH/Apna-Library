from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    Roll_No = models.PositiveIntegerField(null=True, blank=True)
    Date_Of_Birth = models.DateField(null=True, blank=True)
