from django.urls import path, include
from accounts.views import *


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('get_token/', PasswordResetAPIView.as_view(), name='get_token'),
    path('recover_password/', PasswordRecoveryAPIView.as_view(), name='password_recovery'),    
    path('users/<int:pk>', GetUserAPIView.as_view(), name='get_user'),
    path('users/all/', GetUsersListAPIView.as_view(), name='list_users'),
    path('users/delete/', DeleteUserAPIView.as_view(), name='get_user'),
    path('users/update/', UpdateUserAPIView.as_view(), name='update_user'),
    path('skills/', SkillsAPIViews.as_view(), name='skills'),
<<<<<<< HEAD
    path('skills/delete/<int:skill_id>', DeleteSkillAPIView.as_view(), name='delete_skill'),  
   
]
=======
    path('skills/delete/<int:skill_id>', DeleteSkillAPIView.as_view(), name='delete_skill'),    
    path('user/token/',UserByTokenAPIView().as_view(), name='get_user_by_token')
]
>>>>>>> ff374040649c98582a9ccc1bd5cfe1e56a499880
