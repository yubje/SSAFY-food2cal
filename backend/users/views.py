from users.models import Profile
from users.serializers import ProfileSerializer

from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrReadOnly

from rest_framework.viewsets import ModelViewSet

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user, id=user.id)