from . views import *
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('logout/',logout,name="logout"),
    path('profile/',profile,name="profile"),
    path('changepassword/',changepassword,name="changepassword"),




]