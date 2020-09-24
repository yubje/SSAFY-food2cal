from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Diet, Food
from .serializers import DietSerializer, FoodSerializer, DietListSerializer

from posts.models import Post

# 식단 생성 
# @api_view(['POST'])
def diet_create(request, post_id):
    serializer = DietSerializer(data=request.data.get("diet"))
    if serializer.is_valid(raise_exception=True):
        # serializer.save(user=request.user, post_id=post_id)
        serializer.save(post_id=post_id)
        # print(serializer.data)
        # print(request.data["food"])
        for food in request.data["food"]:
            food_create(request, food, serializer.data["id"])
        return Response(serializer.data)

# @api_view(['GET'])
def diet_list(post_id):
    diets = Diet.objects.filter(post_id=post_id)
    serializer = DietListSerializer(diets, many=True)
    # print(serializer.data)
    for i in range(len(serializer.data)):
        serializer.data[i]["food"] = food_list(serializer.data[i]["id"])
    return json.dumps(serializer.data)


# @api_view(['POST']) 
def food_create(request, food, diet_id):
    serializer = FoodSerializer(data=food)
    if serializer.is_valid(raise_exception=True):
        # serializer.save(user=request.user, diet_id=diet_id)
        serializer.save(diet_id=diet_id)
        return Response(serializer.data)

def food_list(diet_id):
    foods = Food.objects.filter(diet_id=diet_id)
    serializer = FoodSerializer(foods, many=True)
    
    food_data = []
    for food in serializer.data:
        food_data.append(dict(food))
    return food_data
