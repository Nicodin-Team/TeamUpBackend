from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from announcements.models import Announcement, AnnouncementJoinRequest
from announcements.serializers import AnnouncementSerializer, AnnouncementJoinRequestSerializer
from rest_framework.response import  Response
from rest_framework import viewsets
from rest_framework import status, viewsets, generics
from accounts.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

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
    

class MyAnnouncementsAPIView(generics.RetrieveAPIView):
    """
    User can get the his/her own announcements.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AnnouncementSerializer
    pagination_class = AnnouncementPagination
    def get(self, request):
        user = request.user
        announcements = Announcement.objects.filter(user=user).order_by('-created_at')
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
    

    
class AnnouncementJoinRequestManagementView(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return AnnouncementJoinRequest.objects.filter(announcement__creator=user)

    def get(self, request):
        join_requests = self.get_queryset()
        serializer = AnnouncementJoinRequestSerializer(join_requests, many=True)
        return Response(serializer.data)

    def patch(self, request, request_id):
        try:
            join_request = AnnouncementJoinRequest.objects.get(pk=request_id)
        except AnnouncementJoinRequest.DoesNotExist:
            return Response({'error': 'Join request not found'}, status=404)

        if join_request.announcement.creator != request.user:
            return Response({'error': 'You are not authorized to manage this join request'}, status=403)

        if request.data.get('status') not in ['ACCEPTED', 'REJECTED']:
            return Response({'error': 'Invalid status. Valid options are ACCEPTED or REJECTED.'}, status=400)

        join_request.status = request.data['status']
        join_request.save()
        serializer = AnnouncementJoinRequestSerializer(join_request)
        return Response(serializer.data)
