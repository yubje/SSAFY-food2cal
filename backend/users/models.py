from django.db import models
from django.contrib.auth.models import AbstractUser

from posts.models import Post


class User(AbstractUser):
    # articles = models.ManyToManyField(Post, through='Vote')
    pass

