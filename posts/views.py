from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status, viewsets, generics

from .serializers import postSerializer,LikeSerializer,CommentSerializer
from .models import Like,Comment,post
from posts.serializers import UserSerializer
from requests.models import Response
# from django.contrib.auth.models import User

from .models import post


class postViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

