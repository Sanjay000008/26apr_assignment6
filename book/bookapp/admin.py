from django.contrib import admin
from .models import *

# Register your models here.

class Abooks(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','title','auther','isbn','publisher']

admin.site.register(books,Abooks)