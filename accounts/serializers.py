from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password','first_name', 'last_name']
        extra_kwargs = {
        'email': {'required': True},
        'username': {'required': True},
        'password': {'required': True, 'write_only': True}
    }
        
    def create(self, validated_data):        
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user