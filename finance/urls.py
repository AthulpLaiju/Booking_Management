from . views import *
from django.urls import path

urlpatterns = [

    path('bookings/',bookings,name="bookings"),
    path('home/',home,name="home"),
    path('viewbook/',viewbook,name="viewbook"),
    path('deletebook/<int:id>',deletebook,name="deletebook"),

 
    


]