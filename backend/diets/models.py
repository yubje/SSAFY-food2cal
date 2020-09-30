from django.db import models
from django.conf import settings
from posts.models import Post

class Diet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = (
        ('MO', '아침'), ('LU', '점심'), ('DI', '저녁'), ('SN', '간식기타')
    )
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    calorie = models.IntegerField()
    carbohydrate = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, null=True)


class Nutrition(models.Model):
    food_name = models.CharField(max_length=100)
    amount = models.IntegerField() 
    calorie = models.IntegerField() 
    carbohydrate = models.IntegerField() 
    protein = models.IntegerField() 
    fat = models.IntegerField() 


