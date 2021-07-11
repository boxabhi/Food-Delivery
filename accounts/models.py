
from django.db import models
from django.contrib.auth.models import User
from home.models import BaseModel
# Shopkeeper , Customer 



class Shopkeeper(User):
    '''
    Shopkeeper model handling restraunt owner
    '''
    phone_number = models.CharField(max_length=10)
    email_token = models.CharField(max_length=100, null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    adhar_card = models.CharField(max_length=16)
    gst_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,
                choices=(('Male' , 'Male'),
                ('Female' , 'Female')))


    class Meta:
        db_table = 'shopkeeper'



class Customer(User):
    phone_number = models.CharField(max_length=10)
    email_token = models.CharField(max_length=100, null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'customer'
    

    def get_cart_count(self):
        try:
            cart = self.customer_cart.get(is_paid = False)
            return cart.cart.count()
        except Exception as e:
            return 0
        return 0

    


class CusomerAddress(BaseModel):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    address = models.TextField()
    pincode = models.CharField(max_length=100)







