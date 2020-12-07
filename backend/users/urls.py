from django.urls import path, include
from . import views

from users.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    # path("", include(router.urls)),
    path('profiles/', views.profile_detail)
]