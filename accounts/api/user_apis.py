from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.Pagination import MediumPage
from accounts.serializers import UserSerializer, UserRegistrationSerializer
from accounts.models import CustomUser


class GetUserAPIView(generics.RetrieveAPIView):
    """
    Retrive a single user's information through this API.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class GetUsersListAPIView(generics.ListAPIView):
    """
    List the users with pagination through this API.
    """    
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    pagination_class = MediumPage
    serializer_class = UserSerializer


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