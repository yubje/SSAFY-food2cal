from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    profile_image_path = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birth = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
    goal = models.IntegerField()

    def __str__(self):
        return self.user.username

