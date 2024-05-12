from django.db import models
from accounts.models import CustomUser
from django.conf import settings

class Announcement(models.Model):
    user =  models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add = True,blank=True, null=True)
    active = models.BooleanField(default=True)

class JoinRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    status_choices = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    )
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

