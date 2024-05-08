from django.urls import path, include
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, JoinRequestViewSet, ManagerJoinRequestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"announcements", viewset=AnnnouncementViewSet, basename="announcements")
router.register(r'join-requests', JoinRequestViewSet, basename='join-request')
router.register(r'manager-join-requests', ManagerJoinRequestViewSet, basename='manager-join-request')

urlpatterns = [
    path('', include(router.urls)),
    path("mine/",MyAnnouncementsAPIView.as_view(), name="my_announcements"),
]

