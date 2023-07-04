from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(max_length=100, unique=True)
    nickname=models.CharField(max_length=100)
    #university=models.CharField(max_length=100)
    #location=models.CharField(max_length=100)
    birth=models.DateTimeField(default=timezone.now())
    age=models.IntegerField(default=20)
    motto=models.CharField(max_length=500, default="안녕")

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200)
    content=models.TextField()

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    created_at=models.DateTimeField(auto_now_add=True)
    content=models.TextField()