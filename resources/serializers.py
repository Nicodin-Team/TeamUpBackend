from rest_framework import serializers
from resources.models import City, SkillName

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class SkillNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillName
        fields = '__all__'
        