from rest_framework import generics
from resources.models import City
from resources.serializers import CitySerializer

class CitiesAPIView(generics.ListAPIView):
    """
    Lists all of the cities as resource for frontend.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer