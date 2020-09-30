from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from rest_framework import mixins

# Create your views here.
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, InOwnProfileOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

@api_view(['POST'])
def profile_create(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        serializer.save()
        return Response(serializer.data)