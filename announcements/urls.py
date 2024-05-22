from django.urls import path, include
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, AnnouncementApply, AddAnnouncement


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"announcements", viewset=AnnnouncementViewSet, basename="announcements")


urlpatterns = [
    path('', include(router.urls)),
    path("mine/",MyAnnouncementsAPIView.as_view(), name="my_announcements"),
    path('<slug:slug>/apply', AnnouncementApply.as_view()),
    path('add', AddAnnouncement.as_view()),

]