from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.pagination import MediumPage
from accounts.serializers import UserSerializer, UserRegistrationSerializer
from accounts.models import CustomUser
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser


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
    filter_backends = [SearchFilter]
    search_fields =  ['username', 'first_name', 'last_name']



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
    Update a single user's information through this API.
    """    
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]

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
    

class FilterUserAPIView(generics.ListAPIView):
    """
    Use this api to filter the user through some parameters such as age, skills, country , city and ...
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['min_age','max_age', 'gender', 'country', 'city', 'skills__name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        min_age = self.request.query_params.get('min_age')
        max_age = self.request.query_params.get('max_age')
        if min_age is not None:
            queryset = queryset.filter(age__gte=min_age)
        if max_age is not None:
            queryset = queryset.filter(age__lte=max_age)

        gender = self.request.query_params.get('gender')
        if gender is not None:
            queryset = queryset.filter(gender=gender)

        skill = self.request.query_params.get('skills__name')
        if skill is not None:
            queryset = queryset.filetr(skill)
        
        search_query = self.request.query_params.get('search')
        if search_query is not None:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset