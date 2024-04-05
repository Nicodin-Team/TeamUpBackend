from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from projects.models import Project
from accounts.serializers import UserSerializer
from accounts.models import CustomUser

class ProjectsUsersAPIView(generics.GenericAPIView):
    """
    Get the users of a project through this API.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, project_id):
        try:        
            project = Project.objects.get(id=project_id)
        except:
            return Response({"message": "no project with given id is found"}, status=status.HTTP_404_NOT_FOUND)
        users = project.users
        serializer = UserSerializer(instance=users, many = True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

