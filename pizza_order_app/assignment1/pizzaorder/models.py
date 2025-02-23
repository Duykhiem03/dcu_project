from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PizzaSize(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class Cheese(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PizzaSauce(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(null=True, max_length=100)
    date_created = models.DateTimeField(auto_now=True)
    address = models.TextField(null=True)
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    crust_type = models.CharField(max_length=100)
    sauce = models.ForeignKey(PizzaSauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Toppings)