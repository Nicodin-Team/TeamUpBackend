from rest_framework import serializers
from chat.models import Room
from accounts.serializers import UserSerializer

class RoomSerializer(serializers.ModelSerializer):
    online = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ['id', 'online']

    # def __init__(self, *args, **kwargs):        
    #     exclude_fields = self.context.get('exclude_fields', None)
    #     super(RoomSerializer, self).__init__(*args, **kwargs)
                
    #     if exclude_fields:
    #         for field in exclude_fields:
    #             self.fields.pop(field, None)