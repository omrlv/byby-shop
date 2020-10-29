from django.contrib import admin
from .models import Bicycle

class CustomAdminPanel(admin.ModelAdmin):
    list_display = ['id', 'name']

# Register your models here.
admin.site.register(Bicycle, CustomAdminPanel)
