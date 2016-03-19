from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','owner','category','price','condition','status','content']


admin.site.register(Product,ProductAdmin)
