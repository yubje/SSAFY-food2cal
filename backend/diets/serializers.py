from rest_framework import serializers
from users.serializers import UserSerializer
# from posts.models import Post
# from posts.serializers import PostSerializer

from .models import Diet

# 식단 리스트
class DietListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        # 게시글 제목이랑 작성자만 보여주기
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')

# 식단 상세정보
class DietSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=False)
    class Meta:
        model = Diet
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'post')


