from django.urls import path
from .views import BookingList,BookingListEdit

urlpatterns=[
    path('',BookingList.as_view()),
    path('bookings',BookingList.as_view())
]