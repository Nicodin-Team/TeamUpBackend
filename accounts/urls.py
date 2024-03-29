from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'), 
    path('get_token', PasswordResetAPIView.as_view(), name='get_token'), 
    path('recover_password', PasswordRecoveryAPIView.as_view(), name='password_recovery'), 
]
