from django.contrib import admin
from announcements.models import Announcement
from announcements.models import Manager, Score

admin.site.register(Announcement)
admin.site.register(Manager)
admin.site.register(Score)
