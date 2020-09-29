from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    profile_image_path = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    goal = models.IntegerField()
    