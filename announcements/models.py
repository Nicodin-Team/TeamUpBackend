from django.db import models
from accounts.models import CustomUser


from django.conf import settings


class Announcement(models.Model):
    user =  models.ForeignKey(CustomUser, related_name='announcements', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add = True,blank=True, null=True)
    active = models.BooleanField(default=True)

from django.db import models
from django.conf import settings

class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account_manager')
    name = models.CharField(max_length=100)

class Score(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='scores')
    value = models.IntegerField()
    date = models.DateField(auto_now_add=True)