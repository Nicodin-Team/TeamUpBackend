from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email,username, password, **other_fields):
        if not email:
            raise ValueError("Email Address must be provided")
        if not password:
            raise ValueError("Password Address must be provided")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()        

        return user
    
    def create_superuser(self, email, username, password, **otherfields):
        otherfields.setdefault('is_active', True)
        otherfields.setdefault('is_staff', True)
        otherfields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **otherfields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add = True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username    

class PasswordResetToken(models.Model):
    email = models.EmailField()
    token = models.CharField()
    expiration = models.DateTimeField()

    def is_expired(self):
        return self.expiration < timezone.now()