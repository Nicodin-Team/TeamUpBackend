from rest_framework import serializers
from announcements.models import Announcement, Manager, Score


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    average_score = serializers.FloatField(read_only=True)

    class Meta:
        model = Manager
        fields = ('id', 'name', 'average_score')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'manager', 'value', 'date')