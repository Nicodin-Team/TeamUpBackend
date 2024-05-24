from django.urls import path, include
<<<<<<< HEAD
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, ManagerListView, BestManagerView
=======
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, AnnouncementJoinView, AnnouncementJoinRequestActionView


>>>>>>> dev
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"announcements", viewset=AnnnouncementViewSet, basename="announcements")


urlpatterns = [
    path('', include(router.urls)),
    path("mine/",MyAnnouncementsAPIView.as_view(), name="my_announcements"),
<<<<<<< HEAD
     path('managers/', ManagerListView.as_view()),
    path('best-manager/', BestManagerView.as_view()),
]

=======
    path('<int:announcement_id>/join/', AnnouncementJoinView.as_view(), name='announcement-join'),
    path('join-requests/<int:join_request_id>/<str:action>/', AnnouncementJoinRequestActionView.as_view()),
]
>>>>>>> dev
