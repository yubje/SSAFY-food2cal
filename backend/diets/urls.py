from django.urls import path
from . import views

app_name = 'diets'

urlpatterns = [
    path('<int:post_id>/', views.diet_list, name='diet_list'),
    path('foods/', views.food_list, name='food_list'),
]

