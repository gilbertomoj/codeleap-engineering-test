from django.shortcuts import render
from .serializer import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def PostListView(request):
    api_urls = {
        'all_posts': '/',
        'add': '/create'
    }

    return Response(api_urls)


@api_view(['GET'])
def PostDetail(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def PostCreateView(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)


@api_view(['PATCH'])
def PostUpdateView(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['DELETE'])
def PostDeleteView(request, pk):
    post = Post(id=pk)
    post.delete()
    return Response(status=204)
