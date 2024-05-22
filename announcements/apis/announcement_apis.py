from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer
from rest_framework.response import  Response
from rest_framework import viewsets
from rest_framework import status, viewsets, generics
from accounts.permissions import IsOwnerOrReadOnly
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





from django.shortcuts import render
from announcements.models import AnnouncementApply, Announcement
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from announcements.forms import AnnouncementForm, AnnouncementApplyForm
from django.db.models import Q, F
from django.db.models.aggregates import Sum, Min, Max, Count, Avg
#brings the normal get but with error handling 404
from django.shortcuts import get_object_or_404


class JobApply(CreateView):
    model = AnnouncementApply
    success_url = '/jobs'
    #fields = ['username', 'email', 'linkedIn_url', 'githup_url', 'cv', 'cover_letter']
    form_class = AnnouncementApplyForm

    def form_valid(self, form):
        # Get the job slug from the URL
        Announcement_slug = self.kwargs.get('slug')

        # Retrieve the job associated with the slug
        announcements = get_object_or_404(Announcement, slug=Announcement_slug)

        # Set the job field in the form to the retrieved job
        form.instance.announcements = announcements

        # Save the form and set the success_url
        response = super().form_valid(form)

        return response
    
class AddAnnouncement(CreateView):
    model = Announcement
    #fields = ['title', 'location', 'company', 'salary_start', 'salary_end', 'description', 'vacancy', 'job_type', 'experience', 'category']
    success_url = '/Announcement/'
    form_class = AnnouncementForm