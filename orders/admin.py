from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CouponCode)


class CartAdmin(admin.ModelAdmin):
    list_display = ['id','customer' , 'is_paid' ,'total_price']
    
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItems)