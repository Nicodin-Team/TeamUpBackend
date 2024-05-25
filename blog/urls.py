from django.urls import path, include
from .views import BlogListAPIView, BlogDetailAPIView, CommentPostAPIView, BlogCRUDAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"", viewset=BlogCRUDAPIView, basename="blogs")


urlpatterns = [
    path('', include(router.urls)),
    path('list/', BlogListAPIView.as_view()),
    path('detail/<int:pk>/', BlogDetailAPIView.as_view()),
    path('comment_create/', CommentPostAPIView.as_view()),
]