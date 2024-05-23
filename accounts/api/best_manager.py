# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Manager
from accounts.serializers import ManagerSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg

class ManagerListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

class BestManagerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        managers = Manager.objects.all()
        best_manager = max(managers, key=lambda x: x.scores.all().aggregate(avg_score=Avg('value'))['avg_score'])
        serializer = ManagerSerializer(best_manager)
        return Response(serializer.data)