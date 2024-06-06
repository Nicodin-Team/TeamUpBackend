from django.urls import path
from resources.views import *

urlpatterns = [
    path("cities/",CitiesAPIView.as_view(), name="list_cities"),
    path("skillset/", SkillsAPIView.as_view(), name="list_skill_set"),
    path('softskills/', SoftSkillsAPIView.as_view(), name='soft_skill_set'),
]