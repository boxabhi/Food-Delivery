


from django.urls import path, include
from .views import *
urlpatterns = [
    path('add-cart/<menu_id>/' , add_cart  , name="add_cart"),
    path('cart/' , cart , name="cart"),
    path('payment-successfull/' , payment_successfull , name="payment_successfull")
]
