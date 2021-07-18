from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from restraunt.models import Restraunt


def home(request):
    print(request.user)
    context = {'restraunts' : Restraunt.objects.all()}
    return render(request , 'home/home.html' , context)

def restraunt_detail(request , slug):
    try:
        restraunt_obj = Restraunt.objects.get(id = slug)
        context = {'restraunt' :restraunt_obj , 'menus' : restraunt_obj.restraunt.all()}
        return render(request , 'home/restraunt_detail.html' , context)
    except Exception as e:
        print(e)

    return redirect('/error/')



def success(request):
    return HttpResponse('Your payment was successfull')

def failure(request):
    return HttpResponse('Your payment was failed')