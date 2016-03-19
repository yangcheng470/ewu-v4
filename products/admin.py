from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','owner','valid','category','price','condition','pub_date','get_content']
    ordering=['id']


admin.site.register(Product,ProductAdmin)
