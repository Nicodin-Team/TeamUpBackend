from django.contrib import admin
from resources.models import City, SkillName, SoftSkillName

admin.site.register(SkillName)
admin.site.register(SoftSkillName)
admin.site.register(City)
