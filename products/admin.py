from django.contrib import admin
from .models import Product

# Register your models here.

def make_sold(modeladmin, request, queryset):
    queryset.update(status='sold')

make_sold.short_description = '标记为售出'


def make_sale(modeladmin, request, queryset):
    queryset.update(status='sale')

make_sale.short_description = '标记为在售'


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','owner','valid','status','category','price','condition','pub_date','visitors','get_content']
    list_display_links = ['id', 'name']
    ordering=['id']
    save_as = True
    actions = [make_sold, make_sale]
    readonly_fields = ['small_img', 'big_img']


admin.site.register(Product,ProductAdmin)
