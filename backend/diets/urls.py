from django.urls import path
from . import views

app_name = 'diets'

urlpatterns = [
    path('<year_month>/', views.diet_calendar, name='diet_calendar'),
    path('foods/', views.food_list, name='food_list'),
]

