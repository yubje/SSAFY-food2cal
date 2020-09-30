from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Diet, Food
from .serializers import DietSerializer, FoodSerializer, DietListSerializer
from users.serializers import UserSerializer

from posts.models import Post

# 식단 생성 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def diet_create(request):
    # User = get_user_model()
    # user = get_object_or_404(User, username=request.user)
    diet_info = request.data.get("diet")
    serializer = DietSerializer(diet_info)
    print(serializer.data)
    diet = Diet.objects.get(user=request.user, created_at__startswith=diet_info["date"], category=diet_info["category"])
    # 이미 저장된 식단이 있는 경우 기존 식단에 음식 추가 
    if diet:
        food_data = food_list(diet.id)
        for food in request.data["food"]:
            food_data.append(food_create(request, food, diet.id))
        print(food_data)

    # 새로 식단을 생성하는 경우 
    elif serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        food_data = []
        for food in request.data["food"]:
            food_data.append(food_create(request, food, serializer.data["id"]))
    return_data = serializer.data
    return_data["food"] = food_data
    return Response(return_data)



@api_view(['GET'])
def diet_calendar(request, year_month):
    diets = Diet.objects.filter(user=request.user, created_at__startswith=year_month)
    serializer = DietListSerializer(diets, many=True)
    for i in range(len(serializer.data)):
        serializer.data[i]["food"] = food_list(serializer.data[i]["id"])
    return Response(serializer.data)

@api_view(['GET'])
def diet_statistics(request):
    diets = Diet.objects.filter(user=request.user).order_by('-pk')[:15]
    serializer = DietListSerializer(diets, many=True)
    return Response(serializer.data)

# post 생성에 사용, api 없음
def food_create(request, food, diet_id):
    serializer = FoodSerializer(data=food)
    if serializer.is_valid(raise_exception=True):
        serializer.save(diet_id=diet_id)
        return serializer.data


# post 상세조회에 사용, api 없음 
def food_list(diet_id):
    foods = Food.objects.filter(diet_id=diet_id)
    serializer = FoodSerializer(foods, many=True)
    food_data = []
    for food in serializer.data:
        food_data.append(dict(food))
    return food_data

@api_view(['DELETE'])
def food_delete(request, diet_id, food_id):
    food = get_object_or_404(Food, pk=food_id)
    diet = get_object_or_404(Diet, pk=diet_id)
    print(food)
    print(diet)
    if request.user == diet.user:
        food.delete()
        return Response({'status': 200})
