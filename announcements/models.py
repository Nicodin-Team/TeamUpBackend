from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.contrib.auth.models import User


class Manager(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="manager")

    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements')

    def __str__(self):
        return self.title

class Score(models.Model):
    value = models.IntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="scores")
    
    def __str__(self):
        return F"{self.manager.name}-{self.value}"



class AnnouncementJoinRequest(models.Model):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='join_requests')
    status = models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)