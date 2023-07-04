from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response

# Create your views here.

class PostListView(views.APIView):
    def get(self,request,format=None):
        posts=Post.objects.all()     
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=PostSerializer(data=request.data)  # 입력받은 게시글 데이터를 시리얼라이저에 넣어 변환
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class PostCateListView(views.APIView):
    def get(self,request,week,format=None):
        #posts=Post.objects.filter(category=request.cate)    # 이러면 프론트에서 그냥 {"cate":"월요일"} 이런식으로 넘기면 쓸 수 있는건가?
        posts=Post.objects.filter(category=week)    #.. 맞나?
        serializer=PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class PostDetailView(views.APIView):
    def get(self,request,pk,format=None):           
        posts=get_object_or_404(Post,pk=pk)           # pk 값 이용해 특정 게시글 객체만 가져오고 
        serializer=PostSerializer(posts)              # 시리얼라이저에 넣어 데이터 변환
        print(serializer)
        return Response(serializer.data)              # serializer.data 로 변환된 데이터 변환
    
    def put(self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # def patch(self, request, pk, format=None):

    def delete(self, request, pk, format=None):
        post=get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({"message":"게시물 삭제 성공"})
    
class CommentView(views.APIView):
    def post(self,request,format=None):
        serializer=CommentSerializer(data=request.data)     # 입력받은 댓글 데이터를 시리얼라이저에 넣어 변환
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def get(self,request,format=None):
        comments=Comment.objects.all()     
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

class CommentDetailView(views.APIView):
    def get(self,request,pk,format=None):           
        comment=get_object_or_404(Comment,pk=pk)           # pk 값 이용해 특정 게시글 객체만 가져오고 
        serializer=CommentSerializer(comment)              # 시리얼라이저에 넣어 데이터 변환
        return Response(serializer.data)              # serializer.data 로 변환된 데이터 변환
    
    def put(self,request,pk,format=None):
        comment=get_object_or_404(Comment, pk=pk)
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    #patch
        
    def delete(self,request,pk,format=None):
        comment=get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({"message":"댓글 삭제 성공"})