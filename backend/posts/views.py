from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostListSerializer, PostSerializer

# 글 리스트 
@api_view(['GET'])
def post_list(request, page_id=0):

    posts = Post.objects.order_by('-pk')[:page_id*10]
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)

# 글 생성 
@api_view(['POST']):
def post_create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 댓글 상세조회 
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.user == post.user:
        # 댓글 수정 
        if request.method == 'PUT':
            serializer = PostSerializer(data=request.data, instance=post)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 'success'})
        # 댓글 삭제 
        elif request.method == 'DELETE':
            post.delete()
            return Response({'message': 'success'})
    else:
        return Response({"status": "FORBIDDEN"})

@api_view(['GET', 'POST'])
def comment_list(request, post_id):
    # 댓글 리스트 반환 
    if request.method == 'GET':
        comments = Comment.objects.filter(post_id=post_id).order_by('-pk')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    # 댓글 생성 
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, post_id=post_id)
        
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        # 댓글 수정 
        if request.method == 'PUT':
            serializer = CommentSerializer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 'success'})
        # 댓글 삭제 
        else:
            comment.delete()
            return Response({'message': 'success'})





