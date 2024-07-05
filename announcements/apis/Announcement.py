from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer
from rest_framework.generics import CreateAPIView , GenericAPIView
from rest_framework.response import  Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework import status


class AnnouncementPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AnnouncementAPIView(GenericAPIView):
    """
    API endpoint for Announcement CRUD operations.
    """
    pagination_class = AnnouncementPagination
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request):
        """
        Retrieve ads based on the employer/user ID.
        """
        creator_id = request.GET.get('creator_id')  # Assuming the query parameter is 'creator_id'
        announcements = self.queryset.filter(creator_id=creator_id)

        # Pagination
        paginator = self.pagination_class()
        paginated_announcements = paginator.paginate_queryset(announcements, request)
        serializer = self.serializer_class(paginated_announcements, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        """
        Create a new announcement.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update an existing announcement (only allowed for the owner).
        """
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({"error": "Announcement not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the request user is the owner of the announcement
        if announcement.creator_id != request.user.id:
            return Response({"error": "You are not allowed to edit this announcement."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an announcement (only allowed for the owner).
        """
        try:
            announcement = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({"error": "Announcement not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the request user is the owner of the announcement
        if announcement.creator_id != request.user.id:
            return Response({"error": "You are not allowed to delete this announcement."}, status=status.HTTP_403_FORBIDDEN)

        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AnnouncementLISTView(viewsets.ModelViewSet):
    
    serializer_class = AnnouncementSerializer 
    @action(detail=False, methods=['get'])
    def search(self, request, title):
        """
        Search announcements based on a query.
        """
        queryset = Announcement.objects.all()
        print(queryset)
        if not queryset.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        announcements = queryset.filter(title__icontains=title)
        serializer = self.get_serializer( announcements , many=True )
        return Response(serializer.data)