from rest_framework import generics, viewsets
from blog.models import Blog, Comment, SubContent, Tag
from blog.serializers import BlogSerializer, BlogDetailSerializer, CommentSerializer, BlogSerializerCreate
from rest_framework.permissions import IsAuthenticated

class BlogCRUDAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class BlogListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/list/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializerCreate


class BlogDetailAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/detail/<int:blog_id>/
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer


class CommentPostAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/blog/comment_create/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer