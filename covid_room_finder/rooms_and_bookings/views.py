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

        #checking request data if valid start--------------------------

        if serializer.is_valid():

            #coverting data in jason for easy readability...........
            
            item = json.dumps(request.data)
            booking_item = json.loads(item)

            # Allowed person in the requested room............
            allowed = Rooms.objects.get(
                roomname=booking_item['room_name']).allowedperson

            # already booked count in that room in that date................
            count = Bookings.objects.filter(
                room_name=booking_item['room_name'], date=booking_item['date']).count()


            #Checking if there is space available in the room and then save the booking................

            if allowed > count:
                serializer.save()
                datas = 'We booked successfully a place in ' + \
                    booking_item['room_name'] + ' on ' + \
                        booking_item['date']+' for you. '
                content = {
                    'confirmed': 'true',
                    'data': datas
                }
                return Response(content, status=201)

            #if there is no available space return who occupied the rooms and avaiable rooms with space...............

            elif allowed <= count:
                availablerooms = ""
                bookedoutby=""
                finalresponse=""

                allrooms = Rooms.objects.all()

                #checking all regular rooms space and room space on a fixed date and cheching if that romm is available..........
                
                for room in allrooms.iterator():
                    allowed1 = Rooms.objects.get(
                        roomname=room.roomname).allowedperson

                    count1 = Bookings.objects.filter(
                        room_name=room.roomname, date=booking_item['date']).count()
                    if allowed1 > count1:
                        availablespace = allowed1 - count1
                        availablerooms = availablerooms + \
                            " [ "+room.roomname+" WITH OPEN PLACES " + \
                            str(availablespace)+" ], "

                #checking who booked out the room on a specific date...................
                
                fullroom = Bookings.objects.filter(
                    room_name=booking_item['room_name'], date=booking_item['date'])
                
                for i in fullroom.iterator():
                    bookedoutby=bookedoutby+" [ "+i.name+" ], "

                print(availablerooms)
                print(bookedoutby)
                finalresponse ="Room is already booked out by "+bookedoutby+" on this day. Try room(s): "+availablerooms


                content = {
                    'confirmed': 'false',
                    'data': finalresponse
                }

                return Response(content)

        return Response(None, status=400)


class Capacity(APIView):

    finalrespponse=""

    def get(self, request, pk):
        total_count = 0
        allrooms = Rooms.objects.all()
        single_day_count = Bookings.objects.filter(date=pk).count()
        for room in allrooms.iterator():
            allowed1 = Rooms.objects.get(roomname=room.roomname).allowedperson
            total_count = total_count+allowed1

        Available_space = ((total_count-single_day_count)/total_count)*100

        finalrespponse="The capacity of free working places on "+pk+ " is "+str(Available_space)+"%"
        return Response(finalrespponse)
