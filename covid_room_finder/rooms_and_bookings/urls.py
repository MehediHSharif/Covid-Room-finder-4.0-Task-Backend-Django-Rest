from django.urls import path
from .views import Booking,Capacity

urlpatterns=[
    path('booking',Booking.as_view()),
    path('capacity/<str:pk>',Capacity.as_view()),
]