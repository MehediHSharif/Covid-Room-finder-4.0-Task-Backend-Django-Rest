from django.shortcuts import render
from rest_framework.views import APIView
from .models import Bookings, Rooms
from .serializers import BookingsSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
# Create your views here.


class Booking(APIView):
    def post(self, request):
        serializer = BookingsSerializer(data=request.data)
        if serializer.is_valid():
            item = json.dumps(request.data)
            booking_item = json.loads(item)
            # Allowed person in the requested room
            allowed = Rooms.objects.get(
                roomname=booking_item['room_name']).allowedperson

            # already booked count in that room in that date
            count = Bookings.objects.filter(
                room_name=booking_item['room_name'], date=booking_item['date']).count()

            if allowed > count:
                serializer.save()
                content={
                    'confirmed':'true',
                    'data': serializer.data
                }
                return Response(content, status=201)

            elif allowed <= count:
                availablerooms = ""
                allrooms = Rooms.objects.all()
                for room in allrooms.iterator():
                    allowed1 = Rooms.objects.get(
                        roomname=room.roomname).allowedperson

                    count1 = Bookings.objects.filter(
                        room_name=room.roomname, date=booking_item['date']).count()
                    if allowed1 > count1:
                        availablerooms = availablerooms+room.roomname+", "

                print(availablerooms)
                content={
                    'confirmed':'false',
                    'data': availablerooms
                }
                

                return Response(content)

        return Response(None, status=400)


class Capacity(APIView):

    def get(self, request, pk):
        total_count = 0
        allrooms = Rooms.objects.all()
        single_day_count = Bookings.objects.filter(date=pk).count()
        for room in allrooms.iterator():
            allowed1 = Rooms.objects.get(roomname=room.roomname).allowedperson
            total_count = total_count+allowed1

        Available_space = ((total_count-single_day_count)/total_count)*100
        return Response(Available_space)
