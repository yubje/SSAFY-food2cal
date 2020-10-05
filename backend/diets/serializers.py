from rest_framework import serializers
from users.serializers import UserSerializer

# from posts.models import Post
# from posts.serializers import PostSerializer

from .models import Diet, Food



# 음식 정보 
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'diet')

# 식단 생성
class DietSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # food = FoodSerializer(many=True, read_only=True)
    class Meta:
        model = Diet
        fields = '__all__'
        read_only_fields = ('id', 'user', 'post')


# 식단 리스트
class DietListSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=True, read_only=True)
    class Meta:
        model = Diet
        # 게시글 제목이랑 작성자만 보여주기
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at', 'updated_at')
