from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    TYPE_CHOICES = (
        (1, '월'),
        (2, '화'),
        (3, '수'),
        (4, '목'),
        (5, '금'),
        (6, '토'),
        (7, '일')
    )
    title=models.CharField(max_length=200)
    date=models.DateTimeField() 
    body=models.TextField()
    #image = models.ImageField(upload_to = "images/", null=True, blank=True)
    category = models.IntegerField(choices=TYPE_CHOICES)
    #category = models.CharField('week',max_length=10,null=True,default='')
    #hashtag=models.ManyToManyField(HashTag)


class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comment',on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)