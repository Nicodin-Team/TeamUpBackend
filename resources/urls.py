from django.urls import path
from resources.views import *

urlpatterns = [
    path("cities/",CitiesAPIView.as_view(), name="list_cities")
]