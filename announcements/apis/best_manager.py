from rest_framework.views import APIView
from rest_framework.response import Response
from announcements.models import Manager, Score
from announcements.serializers import ManagerSerializer
from rest_framework import generics, permissions
from django.db.models import Avg

class BestManagerView(generics.ListAPIView):
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Manager.objects.annotate(average_score=Avg('scores__value')).order_by('-average_score')