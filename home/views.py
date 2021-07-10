from django.shortcuts import render
from restraunt.models import Restraunt


def home(request):
    print(request.user)
    context = {'restraunts' : Restraunt.objects.all()}
    return render(request , 'home/home.html' , context)