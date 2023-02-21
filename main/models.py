from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=64, blank=True, null=True)
    bio = models.TextField(max_length=1024, blank=True, null=True)  

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    temp_file = models.FileField(upload_to='temp/videos/')
    vid = models.CharField(max_length=8)
    video_file = models.CharField(max_length=1024)