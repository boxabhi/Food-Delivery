from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(CouponCode)
admin.site.register(Cart)
admin.site.register(CartItems)