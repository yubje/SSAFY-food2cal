from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer

# Create your views here.
@api_view(['POST'])
def profile_create(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        serializer.save()
        return Response(serializer.data)