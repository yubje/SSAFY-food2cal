from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Diet
from .serializers import DietSerializer


# 식단 생성 
@api_view(['POST'])
def diet_create(request):
    serializer = DietSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save(user=request.user, post=request.post)
        return True
    else:
        return False