from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify

class Project(models.Model):
    PROJECT_STATUS_CHOICES=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    users = models.ManyToManyField(CustomUser, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=PROJECT_STATUS_CHOICES, default='active')
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name