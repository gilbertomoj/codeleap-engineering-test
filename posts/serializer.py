from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        model = Post
        fields = ['title', 'content']