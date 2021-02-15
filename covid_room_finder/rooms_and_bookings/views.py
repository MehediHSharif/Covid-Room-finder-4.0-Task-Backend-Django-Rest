from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Bookings
from .serializers import BookingsSerializer
from rest_framework import permissions
# Create your views here.

class BookingList(ListCreateAPIView):

    serializer_class=BookingsSerializer
    permission_classes =(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Bookings.objects.filter(user=self.request.user)

class BookingListEdit(RetrieveUpdateDestroyAPIView):

    serializer_class=BookingsSerializer
    permission_classes =(permissions.IsAuthenticated,)

    

    def get_queryset(self):
        return Bookings.objects.filter(user=self.request.user)