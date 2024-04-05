from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsOwnerOrReadOnly
from accounts.models import Skill
from accounts.serializers import SkillSerializer


class SkillsAPIViews(APIView):    
    """
    Through this API user can get the details of skills or create a skill.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = SkillSerializer

    def post(self, request):
        user = request.user
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():            
            serialized_data.save(user = user)
            return Response({"message": "skill is added to the user"}, status=status.HTTP_200_OK)
        
        return Response({"message": "the data is invalid"},)

    def get(self, request):
        user = request.user
        skills = user.skills
        serializer = self.serializer_class(instance=skills, many=True)
        return Response(data=serializer.data)
    
class DeleteSkillAPIView(APIView):
    """
    Through this API user can delete a skill with skill_id.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]    
    def delete(self, request, skill_id):
        try:
            skill = Skill.objects.get(id=skill_id, user=request.user)
        except Skill.DoesNotExist:
            return Response({"message": "skill not found"}, status=status.HTTP_404_NOT_FOUND)
        
        skill.delete()
        return Response({"message": "skill deleted successfully"}, status=status.HTTP_204_NO_CONTENT)