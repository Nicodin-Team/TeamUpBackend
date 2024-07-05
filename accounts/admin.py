from django.contrib import admin
from accounts.models import CustomUser, Skill

admin.site.register(CustomUser)
admin.site.register(Skill)