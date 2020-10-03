from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = Profile
    fields = '__all__'
