from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Announcement
from accounts.serializers import AnnouncementSerializer

class AnnouncementAPIView(APIView):
   
    """
    API endpoint for Announcement CRUD operations.
    """
   
    def get(self, request):
        """
        Retrieve ads based on the employer/user ID.
        """
        creator_id = request.GET.get('creator_id')  # Assuming the query parameter is 'creator_id'
        announcements = Announcement.objects.filter(creator_id=creator_id)
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def Create(self, request):

        """
        Create a new announcement.
        """
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def Update(self, request, pk):

        """
        Update an existing announcement.
        """
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({"error": "Announcement not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnnouncementSerializer(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def Delete(self, request, pk):
        
        """
        Delete an announcement.
        """
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({"error": "Announcement not found."}, status=status.HTTP_404_NOT_FOUND)

        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)