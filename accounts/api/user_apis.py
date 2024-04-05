from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from accounts.serializers import UserSerializer, UserRegistrationSerializer
from accounts.models import CustomUser


class GetUserAPIView(generics.RetrieveAPIView):
    """
    Retrive a single user's information through this API.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

################################################################################################
class GetUsersListAPIView(APIView):
    """
    List the users with pagination through this API.
    """    
    permission_classes = [IsAuthenticated]

    def get(self, page_num):
        users = CustomUser.objects.all()
        if not users:
            return Response({'message':'No users found'}, status=status.HTTP_404_NOT_FOUND)
        items_per_page = 2
        paginator = Paginator(users, items_per_page)
        page_objects = paginator(page_num)
        serialized_data = UserSerializer(page_objects.object_list, many=True).data

        return Response(data=serialized_data, status= status.HTTP_200_OK)
################################################################################################    

class DeleteUserAPIView(generics.DestroyAPIView):
    """
    Through this API an authenticated user can delete it self.
    """
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'message': 'User is deleted'}, status=status.HTTP_200_OK)
    

class UpdateUserAPIView(APIView):
    """
    Delete a single user's information through this API.
    """    
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def patch(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User information is updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "The data is not valid"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(APIView):
    """
    This is the api for user registeration.
    handle the password match in the frontend.
    """
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "New User Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)