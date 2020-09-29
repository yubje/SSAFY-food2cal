from django.contrib.auth import get_user_model
from rest_framework import serializers
from .model import Profile


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):   
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializier):
  class Meta:
    model = Profile
    fields = '__all__'