from django.urls import path

from . import views

app_name = 'yolo'
urlpatterns = [
    path('', views.index, name='index'),
    
]