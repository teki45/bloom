from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=64, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)