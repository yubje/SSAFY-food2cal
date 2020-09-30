from django.urls import path
from . import views

app_name = 'diets'

urlpatterns = [
    path('', views.diet_create, name='diet_create'),
    path('<year_month>/', views.diet_calendar, name='diet_calendar'),
    path('statistics/', views.diet_statistics, name='diet_statistics'),
    path('<int:diet_id>/foods/<int:food_id>/', views.food_delete, name='food_delete'),
]

