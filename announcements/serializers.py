from rest_framework import serializers
from announcements.models import Announcement, Manager, Score


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['score']

class ManagerSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)

    class Meta:
        model = Manager
        fields = ['id', 'name', 'scores']