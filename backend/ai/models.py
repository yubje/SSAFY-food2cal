from django.db import models

# Create your models here.
class Nutrition(models.Model):
    food_name = models.CharField(max_length=200)
    amount = models.IntegerField()
    calorie = models.IntegerField()
    carbohydrate = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()