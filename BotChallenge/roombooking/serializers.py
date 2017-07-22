from rest_framework import serializers
from roombooking.models import Room, RoomStatus


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('type', 'floor', 'lan', 'phone', 'projector', 'video_conferencing', )


class RoomStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = ('id', 'room', 'user', 'start_time', 'end_time', 'date', 'occupied', )
