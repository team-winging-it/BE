from rest_framework import serializers
from adventure.models import Room

# Room Serializer


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
