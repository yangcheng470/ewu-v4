from django.contrib import admin
from .models import Account

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display=['id','name','valid','campus','phone','qq', 'email','reg_time','last_ip']
    ordering=['id']
    list_display_links = ['id', 'name']

admin.site.register(Account,AccountAdmin)
