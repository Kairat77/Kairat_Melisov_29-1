from rest_framework import serializers
from .models import Hashtag, Post


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    hashtags_list = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

