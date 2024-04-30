from rest_framework import serializers
from .models import CustomUser, Skill
from django.contrib.auth.hashers import make_password
from .models import Announcement

class UserRegistrationSerializer(serializers.ModelSerializer):     
    class Meta:
        model = CustomUser
        fields = ['profile_phot', 'email', 'password', 'username', 'first_name', 'last_name', 'gender', 'age', 'country', 'city']
        extra_kwargs = {
            'email': {'required': True,},
            'username': {'required': True},
            'password': {'required': True, 'write_only': True}
        }
        
    def create(self, validated_data):        
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'created_at', 'gender', 'age', 'country', 'city']        


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'level']


class PasswordRecoverySerializer(serializers.Serializer):
    token = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True)
    confirm_password = serializers.CharField(required = True)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')
        
        if new_password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        return data

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"
        