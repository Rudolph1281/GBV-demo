from django.contrib import admin
# Register your models here.

from .models import Order,Product,Tag,User

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)