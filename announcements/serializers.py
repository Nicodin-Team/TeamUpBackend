from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description', 'number_of_announcements', 'created_at', 'is_active', 'owner']