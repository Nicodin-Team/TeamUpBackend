from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from announcements.models import Announcement, AnnouncementJoinRequest
from announcements.serializers import AnnouncementSerializer, AnnouncementJoinRequestSerializer
from rest_framework.response import  Response
from rest_framework import viewsets
from rest_framework import status, viewsets, generics
from announcements.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import action
from rest_framework import status, viewsets, generics
from announcements.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter


class AnnouncementPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AnnnouncementViewSet(viewsets.ModelViewSet):
    """
    Announcements CRUD\n 
    Through these apis users can: \n- updata \n- creation \n- deletion \n- listing \n- retreive \n the announcements objects.\n
    Operations that are not in SafeMethods need owner permission.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    filter_backends = [SearchFilter]
    search_fields =  ['title']
    
    def get_queryset(self):
        """
        Optionally restricts the returned announcements to a given title,
        by filtering against a `search` query parameter in the URL.
        """
        queryset = Announcement.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def perform_create(self, serializer):
        """
        Set the owner of the announcement to the current user.
        """
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """
        Update the announcement with the provided data.
        """
        serializer.save()

    def perform_destroy(self, instance):
        """
        Delete the announcement.
        """
        instance.delete()

    

class MyAnnouncementsAPIView(generics.RetrieveAPIView):
    """
    User can get the his/her own announcements.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AnnouncementSerializer
    pagination_class = AnnouncementPagination
    def get(self, request):
        user = request.user
        announcements = Announcement.objects.filter(owner=user).order_by('-created_at')
        data = self.serializer_class(announcements, many=True).data

        return Response({'data': data}, status=status.HTTP_200_OK)





class AnnouncementJoinView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(pk=announcement_id)
        except Announcement.DoesNotExist:
            return Response({'error': 'Announcement not found'}, status=404)

        user = request.user

        # Check if user has already requested to join
        if AnnouncementJoinRequest.objects.filter(user=user, announcement=announcement).exists():
            return Response({'error': 'You have already requested to join this announcement.'}, status=400)

        join_request = AnnouncementJoinRequest.objects.create(user=user, announcement=announcement)
        serializer = AnnouncementJoinRequestSerializer(join_request)
        return Response(serializer.data, status=201)  # Created
    

    
class AnnouncementJoinRequestActionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, join_request_id, action):
        try:
            join_request = AnnouncementJoinRequest.objects.get(pk=join_request_id)
        except AnnouncementJoinRequest.DoesNotExist:
            return Response({'error': 'Join request not found'}, status=404)

        if action == 'accept':
            join_request.status = 'accepted'
            join_request.save()
            return Response({'message': 'Join request accepted'}, status=200)
        elif action == 'reject':
            join_request.status = 'rejected'
            join_request.save()
            return Response({'message': 'Join request rejected'}, status=200)
        else:
            return Response({'error': 'Invalid action'}, status=400)


class AnnouncementJoinRequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, announcement_id):
        try:
            announcement = Announcement.objects.get(pk=announcement_id)
        except Announcement.DoesNotExist:
            return Response({'error': 'Announcement not found'}, status=404)

        join_requests = AnnouncementJoinRequest.objects.filter(announcement=announcement)
        serializer = AnnouncementJoinRequestSerializer(join_requests, many=True)
        return Response(serializer.data, status=200)
