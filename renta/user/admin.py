from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(User)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ('username', 'phone_number', 'is_admin', 'is_vendor', 'is_customer')
    list_filter = ('is_admin', 'is_vendor', 'is_customer')
    search_fields = ['username', 'first_name', 'last_name']

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    list_display = ('user','bio','created_at',)


admin.site.site_header = "Renta Administration Dashboard"
