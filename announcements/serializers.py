from rest_framework import serializers
from announcements.models import Announcement, Manager, Score, AnnouncementJoinRequest
from accounts.serializers import UserSerializer

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['value']
        
class ManagerSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    average_score = serializers.SerializerMethodField()
    user = UserSerializer
    class Meta:
        model = Manager
        fields = ['name', 'scores', 'average_score', 'user']

    def get_average_score(self, obj):
        scores = obj.scores.all()
        if scores:
            return sum(score.value for score in scores) / len(scores)
        return 0

class AnnouncementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description', 'number_of_announcements', 'created_at', 'is_active', 'owner']


class AnnouncementJoinRequestSerializer(serializers.ModelSerializer):
    announcement_title = serializers.CharField(source='announcement.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AnnouncementJoinRequest
        fields = ('id', 'user', 'announcement', 'status', 'created_at', 'announcement_title', 'user_username')