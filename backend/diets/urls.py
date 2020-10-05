from django.urls import path
from . import views

app_name = 'diets'

urlpatterns = [
    path('', views.diet_create, name='diet_create'),
    path('statistics/', views.diet_statistics, name='diet_statistics'),
    path('search/', views.food_search, name='food_search'),
    path('<year_month>/', views.diet_calendar, name='diet_calendar'),
    path('<int:diet_id>/foods/<int:food_id>/', views.food_delete, name='food_delete'),

]

