from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('get_token/', PasswordResetAPIView.as_view(), name='get_token'),
    path('recover_password/', PasswordRecoveryAPIView.as_view(), name='password_recovery'),
    path('users/<int:pk>', GetUserAPIView.as_view(), name='get_user'),
    path('users/all/<int:page_num>', GetUsersListAPIView.as_view(), name='list_users'),
    path('users/delete/', DeleteUserAPIView.as_view(), name='get_user'),
    path('users/update/', UpdateUserAPIView.as_view(), name='update_user'),
    path('skills/', SkillsAPIViews.as_view(), name='skills'),
    path('skills/delete/<int:skill_id>', DeleteSkillAPIView.as_view(), name='delete_skill'),
    path('advertisements/<int:creator_id>/', AdvertisementsAPIView.as_view(), name='advertisements'),
]
