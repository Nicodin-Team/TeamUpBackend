from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
<<<<<<< HEAD
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


User = get_user_model()
=======
from django.conf import settings
<<<<<<< HEAD

class Manager(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="manager", limit_choices_to={'is_manager': True})
=======
from django.contrib.auth.models import User
>>>>>>> ff374040649c98582a9ccc1bd5cfe1e56a499880
>>>>>>> dev

class Announcement(models.Model):
    user = models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE, null=True, limit_choices_to={'is_manager': True})
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add = True,blank=True, null=True)
    active = models.BooleanField(default=True)
<<<<<<< HEAD
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE, null = True)

class Score(models.Model):
    value = models.IntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="scores")
=======


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
>>>>>>> dev
