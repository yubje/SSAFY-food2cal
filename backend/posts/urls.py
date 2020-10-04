from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('pages/<int:page_id>/', views.post_list, name='post_list'),
    path('', views.post_create, name='post_create'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/comments/', views.comment_list, name='comment_list'),
    path('<int:post_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('<int:post_id>/votes/<int:vote_id>/', views.vote, name='vote'),
]

