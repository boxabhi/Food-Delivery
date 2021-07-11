from django.db import models
from accounts.models import Shopkeeper
from home.models import BaseModel
from django.utils.text import  slugify


class FoodItem(BaseModel):
    food_item_type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.food_item_type


class Restraunt(BaseModel):
    shopkeeper = models.OneToOneField(Shopkeeper , related_name='shopkeeper' , on_delete=models.CASCADE)
    restraunt_name = models.CharField(max_length=100)
    restraunt_descripton = models.TextField()
    slug = models.SlugField(unique=True ,null=True , blank=True )
    restraunt_address = models.TextField()
    restraunt_pincode = models.CharField(max_length=100)
    restraunt_rating = models.IntegerField(default=-1)
    lattitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    restraunt_image = models.ImageField(upload_to = 'restraunt')


    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.restraunt_name


    def save(self , *args , **kwargs):
        self.slug = slugify(self.restraunt_name)
        super(Restraunt , self).save(*args , **kwargs)        


    def get_menus(self):
        return RestrauntMenu.objects.filter(restraunt = self)


class RestrauntMenu(BaseModel):
    restraunt = models.ForeignKey(Restraunt , related_name='restraunt' , on_delete=models.CASCADE)
    food_item_type = models.ForeignKey(FoodItem , on_delete=models.SET_NULL , null=True , blank=True)
    menu_price = models.IntegerField()
    menu_name = models.CharField(max_length=100)
    menu_description =models.CharField(max_length=100)
    menu_type = models.CharField(max_length=100 , choices=(('Veg'  , 'Veg') , ('Non Veg' , 'Non Veg')) , default='Veg')
    menu_image = models.ImageField(upload_to='menu')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.menu_name


