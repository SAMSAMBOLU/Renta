from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Equipment)
class EquipmentAdmin(ImportExportModelAdmin):
    list_display = ('equipment_name', 'equipment_description', 'equipment_image', 'equipment_price', 'equipment_status', 'equipment_quantity', 'equipment_manufacturer')

@admin.register(Manufacturer)
class Manufacturer(ImportExportModelAdmin):
    list_display = ('manufacturer_name', 'manufacturer_description')

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('user', 'equipment', 'order_date', 'return_date', 'quantity', 'address')