from django.urls import path
from chat.views import ListRoomsAPIView, GetOrCreateRoom

urlpatterns= [
    path('room/list/',ListRoomsAPIView.as_view() , name='list_rooms'),
    path('room/<str:room_name>/',GetOrCreateRoom.as_view() , name='get_room'),
]