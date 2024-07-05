from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from announcements.models import Manager, Score
from announcements.serializers import ManagerSerializer, ScoreSerializer

class ManagerListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            managers = Manager.objects.all()
        except:
            return Response({"message": "No manager exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

class BestManagerView(APIView):

    def get(self, request):
        
        managers = Manager.objects.all()        
        if managers:
            best_manager = max(managers, key=lambda x: x.scores.all().aggregate(avg_score=Avg('value'))['avg_score'])
        else:
            return Response({"message": "No manager exists"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ManagerSerializer(best_manager)
        return Response(serializer.data)
    

class AddScoreView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        manager = Manager.objects.get(user=request.user)
        score = Score.objects.create(manager=manager, value=request.data['value'])
        serializer = ScoreSerializer(score)
        return Response(serializer.data)    