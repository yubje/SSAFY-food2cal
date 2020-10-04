from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username')

class ProfileSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = Profile
    fields = '__all__'
