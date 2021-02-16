from django.db import models
from django.contrib. auth.models import User

# Create your models here.
class Rooms(models.Model):
    roomname=models.CharField(max_length = 255)
    allowedperson=models.IntegerField()

    def __str__(self):
        return self.roomname

class Bookings(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    room_name = models.CharField(max_length = 255,null=True)
    date = models.CharField(max_length = 255,null=True)
    name = models.CharField(max_length = 255,null=True)
    def __str__(self):
        return self.room_name+ " "+self.date