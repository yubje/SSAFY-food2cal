from django.db import models
from django.contrib.auth.models import AbstractUser

from articles.models import Article, Vote


class User(AbstractUser):
  articles = models.ManyToManyField(Article, through='Vote')

