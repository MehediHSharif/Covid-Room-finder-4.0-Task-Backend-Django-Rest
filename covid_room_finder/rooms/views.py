from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from rooms_and_bookings.models import Rooms,Bookings

# Create your views here.

class Allrooms(APIView):
    def get(self,request):
        allrooms = Rooms.objects.all()
        print(allrooms)
        roomsarray=[]
        for rooms in allrooms:
            roomsarray.append(rooms.roomname)
        print(roomsarray)
        return Response(roomsarray)

