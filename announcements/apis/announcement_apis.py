from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response 
from rest_framework import status
from announcements.models import Announcement, JoinRequest
from announcements.serializers import AnnouncementSerializer, JoinRequestSerializer
from rest_framework.generics import CreateAPIView , GenericAPIView
from rest_framework.response import  Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status, viewsets, generics
from accounts.permissions import IsOwnerOrReadOnly, IsManagerOrReadOnly, IsRequestOwnerOrManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class AnnouncementPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AnnnouncementViewSet(viewsets.ModelViewSet):
    """
    Through these apis users can \n- updata \n -creation \n -deletion \n -listing \n -retreive \nthe announcements objects.\n
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
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]
    serializer_class = AnnouncementSerializer
    pagination_class = AnnouncementPagination
    def get(self, request):
        user = request.user
        announcements = Announcement.objects.filter(owner=user).order_by('-created_at')
        data = self.serializer_class(announcements, many=True).data

        return Response({'data': data}, status=status.HTTP_200_OK)
    
class JoinRequestViewSet(viewsets.ModelViewSet):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ManagerJoinRequestViewSet(viewsets.ModelViewSet):
    queryset = JoinRequest.objects.all()
    serializer_class = JoinRequestSerializer
    permission_classes = [IsAuthenticated]


    def perform_update(self, serializer):
        serializer.save(is_accepted=True)