from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','favorite','password']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','post','author','content','created_at']

class PostSerializer(serializers.ModelSerializer):
    comment=CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model=Post
        fields=['id','title','category','author','content','created_at','comment']

    def create(self, validated_data):
        user=User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=64)
    password=serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email=data.get("email", None)
        password=data.get("password", None)

        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError()
            else:
                return user