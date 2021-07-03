from django.contrib import admin
from .models import *


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    pass

class RestrauntMenuAdmin(admin.StackedInline):
    model = RestrauntMenu


@admin.register(Restraunt)
class RestrauntAdmin(admin.ModelAdmin):
    inlines = [ RestrauntMenuAdmin ]
    