from django.urls import path, include
from home.views import *
urlpatterns = [
    path('' , home),
    path('restraunt-detail/<slug>/' , restraunt_detail , name="restraunt_detail"),
    path('success/' , success , name="success"),
    path('failure/' , failure , name="failure")
]
