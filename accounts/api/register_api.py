from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from accounts.models import CustomUser



class RegisterAPIView(APIView):
    """
    This is the api for for user register.
    """
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "New User Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)