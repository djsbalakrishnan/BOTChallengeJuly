from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    room_choices = (
        ('H','Huddle Room'),
        ('T', 'Team Room'),
        ('C', 'Conference Room'),
    )
    floor_choices = (
        (1, 'First Floor'),
        (2, 'Second Floor'),
        (3, 'Third Floor')
    )
    room_number = models.CharField(max_length=10, blank=False, null=False)
    type = models.CharField(max_length=1, choices=room_choices, blank=False, null=False)
    floor = models.IntegerField(choices=floor_choices, blank=False, null=False)
    lan = models.BooleanField(blank=False, null=False)
    phone = models.BooleanField(blank=False, null=False)
    projector = models.BooleanField(blank=False, null=False)
    video_conferencing = models.BooleanField(blank=False, null=False)


class RoomStatus(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    occupied = models.BooleanField(default=False, blank=False, null=False)
