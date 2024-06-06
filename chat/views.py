from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from chat.models import Room
from chat.serializers import RoomSerializer

class ListRoomsAPIView(ListAPIView):
    queryset = Room.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

class GetOrCreateRoom(APIView):
    serializer_class = RoomSerializer
    # permission_classes = [IsAuthenticated]
    def get(self, request, room_name):
        try:
            room = Room.objects.get(name=room_name)        
            room.save()
            data = self.serializer_class(room).data
            return Response({'data': data}, status=status.HTTP_200_OK)
        except Room.DoesNotExist:
            new_room = Room.objects.create(name = room_name)

        data = self.serializer_class(new_room).data

        return Response({'data':data}, status=status.HTTP_201_CREATED)