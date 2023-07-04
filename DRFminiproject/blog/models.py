from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class User(AbstractUser):
    nickname=models.CharField(max_length=10) #닉네임
    favorite=models.CharField(max_length=50) #최애배우
    interest=models.CharField(max_length=30) #최애극

class Blog(models.Model):
    type = models.CharField(max_length=200,default='') #공연명
    title = models.CharField(max_length=200,default='') #게시물 제목
    date = models.DateTimeField('date published') #게시 날짜
    body = models.TextField('Content',default='') #본문

    class Meta:
        ordering = ['date']

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    comment_text = models.TextField()
