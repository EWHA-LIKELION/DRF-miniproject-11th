from .views import *
from django.urls import path

app_name='blog'

urlpatterns=[
    path('posts/', PostListView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('comments/',CommentView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]