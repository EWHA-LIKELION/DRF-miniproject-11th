from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):            # 댓글 시리얼라이저
    class Meta:
        model=Comment
        fields=['id','post','username','comment_text','created_at']


class PostSerializer(serializers.ModelSerializer):               # 게시글 시리얼라이저
    comment=CommentSerializer(many=True, read_only=True)         #중첩 시리얼라이저 1:N관계
    class Meta:
        model=Post
        #fields=['id','title','date','body','image','category','comment']
        fields=['id','title','date','body','category','comment']