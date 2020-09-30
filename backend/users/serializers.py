from django.contrib.auth import get_user_model
from rest_framework import serializers
from .model import Profile

class ProfileSerializer(serializers.ModelSerializier):
  user = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = Profile
    fields = '__all__'