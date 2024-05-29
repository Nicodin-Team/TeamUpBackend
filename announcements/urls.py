from django.urls import path, include
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, AnnouncementJoinView, AnnouncementJoinRequestActionView, AnnouncementJoinRequestListView


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"announcements", viewset=AnnnouncementViewSet, basename="announcements")


urlpatterns = [
    path('', include(router.urls)),
    path("mine/",MyAnnouncementsAPIView.as_view(), name="my_announcements"),
    path('join/<int:announcement_id>/', AnnouncementJoinView.as_view(), name='announcement-join'),
    path('join-requests-list/<int:announcement_id>/', AnnouncementJoinRequestListView.as_view(), name='announcement-join-request-list'),
    path('join-requests-action/<int:join_request_id>/<str:action>/', AnnouncementJoinRequestActionView.as_view()),
]