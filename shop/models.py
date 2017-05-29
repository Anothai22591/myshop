from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100) 
    phone = models.CharField(max_length=100) 
    username = models.CharField(max_length=100) 
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Type_menu(models.Model):
    types = models.CharField(max_length=100) 
    def __str__(self):
        return self.types

class Menu(models.Model):
    type_text = models.ForeignKey(Type_menu)
    menu_text = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.menu_text

class Order_user(models.Model):
    Order_user_text = models.CharField(max_length=100)
    Delivery_location = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    def __str__(self):
        return self.Order_user_text 
class Order(models.Model):
    order = models.ForeignKey(Order_user)
    order_text = models.CharField(max_length=100) 
    def __str__(self):
        return self.order_text




