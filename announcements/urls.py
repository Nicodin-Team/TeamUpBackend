from django.urls import path, include
from announcements.views import AnnnouncementViewSet, MyAnnouncementsAPIView, send_join_request, manage_join_request


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix=r"announcements", viewset=AnnnouncementViewSet, basename="announcements")


urlpatterns = [
    path('', include(router.urls)),
    path("mine/",MyAnnouncementsAPIView.as_view(), name="my_announcements"),
    path('announcement/<int:announcement_id>/request/', send_join_request),
    path('request/<int:request_id>/', manage_join_request),
]