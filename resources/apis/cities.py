from rest_framework import generics
from resources.models import City, SkillName
from resources.serializers import CitySerializer, SkillNameSerializer

class CitiesAPIView(generics.ListAPIView):
    """
    Lists all of the cities as resource for frontend.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

class SkillsAPIView(generics.ListAPIView):
    """
    Lists the skill set
    """
    queryset = SkillName.objects.all()
    serializer_class = SkillNameSerializer