from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializer import PostSerializer
from .models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



