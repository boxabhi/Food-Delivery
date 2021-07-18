from django import urls
from django.shortcuts import redirect, render
from .models import *
from restraunt.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def add_cart(request , menu_id):
    print(request.user.customer)
    try:
        customer = request.user.customer
        cart_obj, _ =  Cart.objects.get_or_create(customer = customer , is_paid = False)
        menu_obj = RestrauntMenu.objects.get(id = menu_id)

        if cart_obj.cart.filter(restraunt_menu = menu_obj).exists():
            cart_item_obj = CartItems.objects.get(
                cart = cart_obj,
                restraunt_menu = menu_obj)
            cart_item_obj.quantity += 1 
            cart_item_obj.save()
        else:
            CartItems.objects.create(
                cart = cart_obj,
                restraunt_menu =menu_obj )

    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
