from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializer import PostSerializer, PostUpdateSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_summary="Get all posts",
    responses={200: PostSerializer(many=True)}
)
@api_view(['GET'])
def PostListView(request):
    api_urls = {
        'all_posts': '/',
        'add': '/create'
    }
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='get',
    operation_summary="Retrieve details of a specific post",
    responses={200: PostSerializer()}
)
@api_view(['GET'])
def PostDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@swagger_auto_schema(
    method='post',
    operation_summary="Create a new post",
    request_body=PostSerializer,
    responses={
        201: PostSerializer(),
        400: "Post with this username already exists"
    }
)
@api_view(['POST'])
def PostCreateView(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='patch',
    operation_summary="Update an existing post",
    request_body=PostUpdateSerializer,
    responses={
        200: PostSerializer(),
        400: "Invalid data or partial content.",
        404: "Post not found."
    }
)
@api_view(['PATCH'])
def PostUpdateView(request, pk):
    post = get_object_or_404(Post, id=pk)  # Retorna 404 se o post não existir
    serializer = PostUpdateSerializer(instance=post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='delete',
    operation_summary="Delete a post",
    responses={
        204: "Post deleted successfully",
        404: "Post not found."
    }
)
@api_view(['DELETE'])
def PostDeleteView(request, pk):
    try:
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=204, data={})
    except Post.DoesNotExist:
        return Response(status=404, data={"detail": "Post not found", "status": 404})
