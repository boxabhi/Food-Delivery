from django.conf import UserSettingsHolder
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from.models import *
import uuid
from django.contrib import messages


def register(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password= request.POST.get('password')
        phone_number=request.POST.get('phone_number')
        email_token=uuid.uuid4()

        if Customer.objects.filter(username=email).exists():
            messages.info(request, 'customer already exists')
            return redirect('/accounts/register/')

        cust_obs=Customer.objects.create(
            email=email,
            username=email,
            phone_number=phone_number,
            email_token=email_token)

        cust_obs.set_password(password)
        cust_obs.save()
        messages.info(request, 'customer register succesfully')
        return redirect('/accounts/login/')

    return render(request, 'accounts/register.html')


def verify_customer_account(request , token):
    try:
        user_obj = Customer.objects.get(email_token = token)
        user_obj.email_verified = True
        user_obj.save()
        return HttpResponse('Your account is verified succesfully')
    except :
        return HttpResponse('Invalid token')

def login_attempt(request):
    try:            
        if request.method == 'POST':
            email = request.POST.get('email')
            password= request.POST.get('password')

            if not email or not password:
                messages.info(request, 'Email and password both are required.')
                return redirect('/accounts/login/')
            custome_obj =Customer.objects.filter(username=email)
            if not custome_obj.exists() :
                return redirect('/accounts/login/')

            
            user=authenticate(username=email,password=password)

            if user is None:
                messages.info(request, 'Invalid password')
                return redirect('/accounts/login/')


            login(request,user)
            messages.success(request, ('welcome Customer'))
            return redirect('/')
    except Exception as e:
        print(e)
    return render(request,'accounts/login.html')

def Shopkeeper_profile(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password= request.POST.get('password')
        username=request.POST.get('username')
        phone_number=request.POST.get('phone_number')
        email_token=uuid.uuid4()

        if Shopkeeper.objects.filter(email=email).first():
            return redirect('/shopkeeper-profile/')

        if Shopkeeper.objects.filter(username=username).first():
            return redirect('/shopkeeper-profile/')

        shopkeeper_obs=Shopkeeper.objects.create(
            email=email,
            username=username,
            phone_number=phone_number,
            email_token=email_token
            )

        shopkeeper_obs.set_password(password)
        shopkeeper_obs.save()
        messages.success(request, ('Your profile was successfully created!,please check your mail'))
        return redirect('../login/')
    return render(request, 'accounts/profile.html')


def verify_shopkeeper_account(request , token):
    try:
        user_obj = Shopkeeper.objects.get(email_token = token)
        user_obj.email_verified = True
        user_obj.save()
        return HttpResponse('Your account is verified succesfully')
    except :
        return HttpResponse('Invalid token')

def login_shopkeeper(request):
    try:
            
        if request.method == 'POST':
            username = request.POST.get('username')
            password= request.POST.get('password')

            if not username or not password:
                return redirect('/login/')
            shopk_objs=Shopkeeper.objects.filter(username=username).first()
            if shopk_objs is None:
                return redirect('/login/')
            
            user=authenticate(username=username,password=password)

            if user is None:
                return redirect ('/login/')

            login(request,user)
            messages.success(request, ('welcome shopkeeper'))
            return redirect('/restaurant/add-restaurant/')
    except Exception as e:
        print(e)
    return render(request,'accounts/login.html')

from django.contrib.auth import logout

def signout(request):
    logout(request)
    return redirect('/home/')

def forget_password(request):
    try:
        if request.method == 'POST':
            username=request.POST.get('username')

            if not Shopkeeper.objects.filter(username=username).first():
                messages.success(request, ('User with this username not found'))
                return redirect('/accounts/forgot-password/')
            user_obj=Shopkeeper.objects.get(username=username)
            token=str(uuid.uuid4())
            send_forgt_password_email(user_obj,token)
            messages.success(request, ('please check your mail'))
            return redirect('/accounts/forgot-password/')

    except Exception as e:
        print(e)
    return render(request,'accounts/forgotpassword.html')