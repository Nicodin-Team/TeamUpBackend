from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),    
]
