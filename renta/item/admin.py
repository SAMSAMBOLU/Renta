from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('item_name', 'item_description', 'item_image', 'item_price', 'item_status', 'item_quantity', 'item_manufacturer')

@admin.register(Manufacturer)
class Manufacturer(ImportExportModelAdmin):
    list_display = ('manufacturer_name', 'manufacturer_description')

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('user', 'item', 'order_date', 'return_date', 'quantity', 'address')