from django.db import models
from django.contrib. auth.models import User

# Create your models here.
class Rooms(models.Model):
    roomname=models.CharField(max_length = 255)
    allowedperson=models.IntegerField()

class Bookings(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    room_name = models.ForeignKey(Rooms,on_delete=models.SET_NULL,null=True)
    date=models.DateField()
    name=models.CharField(max_length = 255)