from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PizzaSize)
admin.site.register(Cheese)
admin.site.register(PizzaSauce)
admin.site.register(Toppings)
admin.site.register(Order)
