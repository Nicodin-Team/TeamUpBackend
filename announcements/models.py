from django.db import models
from accounts.models import CustomUser

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    number_of_announcements = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements')

    def __str__(self):
        return self.title