from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Advertisement
from accounts.serializers import AdvertisementSerializer

class AdvertisementsAPIView(APIView):
    """
    API endpoint to retrieve advertisements based on Creator_id.
    """
    def get(self, request, creator_id):
        advertisements = Advertisement.objects.filter(Creator_id=creator_id)
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)