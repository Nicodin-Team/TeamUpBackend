from rest_framework.views import APIView
from rest_framework.response import Response
from announcements.models import Manager, Score
from announcements.serializers import ManagerSerializer


from rest_framework.response import Response
from django.db.models import Avg

class BestManagerView(APIView):
    def get(self, request, format=None):
        managers = Manager.objects.annotate(average_score=Avg('scores__value'))
        best_manager = managers.order_by('-average_score').first()
        serializer = ManagerSerializer(best_manager)
        return Response(serializer.data)