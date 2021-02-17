from django.urls import path
from .views import Allrooms

urlpatterns=[
    path('allrooms/',Allrooms.as_view()),
]