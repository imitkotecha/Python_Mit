from django.contrib import admin
from .models import *
# Register your models here.

class signuup(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','mobile']


admin.site.register(signupinfo,signuup)