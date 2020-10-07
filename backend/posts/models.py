from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from django.core.cache import cache


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    diet_image_path = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        cache.delete(f'comment_{post.id}')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete(f'comment_{post.id}')
        super().delete(*args, **kwargs)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    def __str__(self):
        return '%s: %d' % (self.post, self.vote)