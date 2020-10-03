from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment, Vote
from .serializers import PostListSerializer, PostSerializer, PostUpdateSerializer, CommentListSerializer, CommentSerializer, CommentUpdateSeriailzer, VoteSerializer

from diets.models import Diet, Food
from diets.serializers import DietListSerializer, FoodSerializer
from diets.views import diet_create, food_list

# 글 리스트 
@api_view(['GET'])
def post_list(request, page_id=0):
    posts = Post.objects.order_by('-pk')[:page_id*5+1]
    print(posts)
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)

# 글 생성 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        # serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 상세조회 
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.user == post.user:
        # 댓글 수정 
        if request.method == 'PUT':
            serializer = PostUpdateSerializer(data=request.data, instance=post)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': 200})
        # 댓글 삭제 
        elif request.method == 'DELETE':
            post.delete()
            return Response({'message': 200})
    else:
        return Response({"status": 401})

@api_view(['GET', 'POST'])
def comment_list(request, post_id):
    # 댓글 리스트 반환 
    if request.method == 'GET':
        comments = Comment.objects.filter(post_id=post_id).order_by('-pk')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    # 댓글 생성 
    elif request.method == 'POST':
        print(request.data)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, post_id=post_id)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        # 댓글 수정 
        if request.method == 'PUT':
            serializer = CommentUpdateSeriailzer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'status': 200})
        # 댓글 삭제 
        else:
            comment.delete()
            return Response({'status': 200})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def vote(request, post_id, vote_id=0):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        votes = Vote.objects.filter(post=post.id)
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data)
    elif request.method in ['POST', 'PUT']:
        vote = get_object_or_404(Vote, post=post.id)
        if vote_id == 0:
            vote.delete()
            return Response({'status': 200})
        elif vote:
            print(vote.vote)
            if vote_id != vote.vote:
                serializer = VoteSerializer(data=request.data, instance=vote)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=request.user)
                    return Response(serializer.data)
            else:
                post.vote.remove()
        else:
            print('else')
            serializer = VoteSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
            print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        vote = Vote.objects.filter(user=request.user, post=post.id)
        vote.delete()
        return Response({'status': 200})



        
    
    # if request.method == 'GET':
    #     vote = Vote.objects.get_or_create(user=request.user, post_id=post_id)
    #     serializer = VoteSerializer(vote)
    #     return Response(serializer.data)
    # elif request.method == 'POST' or request.method == 'PUT':
    #     vote = Vote.objects.get_or_create(user=request.user, post_id=post_id)
    #     pass
    # elif request.method == 'PUT':
    #     pass
    # elif request.method == 'DELETE':
    #     pass






