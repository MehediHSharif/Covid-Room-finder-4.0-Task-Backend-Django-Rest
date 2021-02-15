from rest_framework.serializers import ModelSerializer
from .models import Bookings

class BookingsSerializer(ModelSerializer):

    class Meta:
        model = Bookings
        fields =['room_name','date','name']
