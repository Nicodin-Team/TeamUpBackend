from django.db import models
from accounts.models import CustomUser

class Announcement(models.Model):
    user =  models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add = True,blank=True, null=True)
    active = models.BooleanField(default=True)
