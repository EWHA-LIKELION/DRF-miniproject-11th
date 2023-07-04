from rest_framework import serializers
from blog.models import Blog, Comment, LANGUAGE_CHOICES, STYLE_CHOICES

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'username', 'created_at','comment_text']


class BlogSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'type', 'title', 'date', 'body']

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance


