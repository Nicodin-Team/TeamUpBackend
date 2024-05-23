from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


User = get_user_model()

class Announcement(models.Model):
    user =  models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add = True,blank=True, null=True)
    active = models.BooleanField(default=True)


class AnnouncementJoinRequest(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='join_requests')
    status = models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
