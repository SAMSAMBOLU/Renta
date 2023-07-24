from django.db import models
from user.models import *

# Create your models here.

ITEM_STATUS_CHOICES = [
    ('available', 'AVAILABLE'),
    ('unavailable', 'UNAVAILABLE'),
    ('pending', 'PENDING'),
]

class Item(models.Model):
    item_name = models.CharField(max_length=250, blank=False, null= False)
    item_description = models.TextField()
    item_image = models.ImageField(upload_to='images/', blank= False, null= False)
    item_price = models.IntegerField(blank=False, null= False)
    item_status = models.CharField(max_length=250, choices=ITEM_STATUS_CHOICES)
    item_quantity = models.IntegerField(blank=False, null=False)
    item_manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=250, blank=False, null= False)
    manufacturer_description = models.TextField()

class Order(models.Model):
    user = models.ForeignKey(User, related_name= 'user_item_ordered', on_delete=models.CASCADE)
    item = models.ForeignKey(Item,blank=False, null=False, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    return_date = models.DateTimeField(blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)
    address = models.TextField()

    

