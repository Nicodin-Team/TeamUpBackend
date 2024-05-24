from django.urls import path, include
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, ManagerListView, BestManagerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"announcements", viewset=AnnnouncementViewSet, basename="announcements")


urlpatterns = [
    path('', include(router.urls)),
    path("mine/",MyAnnouncementsAPIView.as_view(), name="my_announcements"),
     path('managers/', ManagerListView.as_view()),
    path('best-manager/', BestManagerView.as_view()),
]

