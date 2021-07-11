from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('login/' , login_attempt , name="login"),
    path('register/' , register , name="register"),
    path('signout/' , signout, name="signout"),
    path('reset-password/<token>/' , reset_password , name="reset_password")

]