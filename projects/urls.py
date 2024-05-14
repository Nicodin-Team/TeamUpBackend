from rest_framework.urls import path
from rest_framework import urlpatterns
from projects.views import ProjectsUsersAPIView

urlpatterns = [
    path('users/<int:project_id>', ProjectsUsersAPIView.as_view(), name='project_users')
]