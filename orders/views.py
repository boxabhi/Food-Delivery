from django import urls
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from restraunt.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))




def cart(request):
    try:
        cart_obj = Cart.objects.get(customer = request.user.customer , is_paid = False)
        payment = client.order.create(
            {'amount' : cart_obj.total_price * 100 , 'currency' : 'INR' , 'payment_capture' :1 }
        )
        cart_obj.razor_pay_order_id = payment['id']
        cart_obj.save()
        
        context = {'carts' : cart_obj , 'order_id':payment['id'] , 'key_id' : settings.KEY_ID}
        
        return render(request , 'cart/cart.html' , context)
    except Exception as e:
        print(e)
    
    return HttpResponse('Your cart is empty')


def payment_successfull(request):
    try:
        razor_pay_order_id = request.GET.get('razorpay_order_id')
        razorpay_payment_id = request.GET.get('razorpay_payment_id')
        razorpay_signature = request.GET.get('razorpay_signature')   
        cart_obj = Cart.objects.get(razor_pay_order_id = razor_pay_order_id)
        cart_obj.is_paid = True
        cart_obj.razorpay_payment_id = razorpay_payment_id
        cart_obj.razorpay_signature = razorpay_signature
        cart_obj.save()
        return redirect('/success/')
    except Exception as e:
        print(e)
    
    return HttpResponse('Something went wrong')



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
