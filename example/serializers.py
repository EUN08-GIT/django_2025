#serializer.py
from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'#다 가져올때,#원하는것만 가져올때 >> ['title',...'author']


