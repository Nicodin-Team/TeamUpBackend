from django.db import models
from accounts.models import CustomUser
from django.conf import settings

class Manager(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="manager", limit_choices_to={'is_manager': True})

class Announcement(models.Model):
    user = models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE, null=True, limit_choices_to={'is_manager': True})
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add = True,blank=True, null=True)
    active = models.BooleanField(default=True)
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE, null = True)

class Score(models.Model):
    value = models.IntegerField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="scores")