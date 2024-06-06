from rest_framework import generics
from resources.models import City, SkillName, SoftSkillName
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

class SoftSkillsAPIView(generics.ListAPIView):
    """
    Lists the soft skill set
    """
    queryset = SoftSkillName.objects.all()
    serializer_class = SkillNameSerializer
