from django.contrib import admin
from .models import Account

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display=['name','campus','phone','email','reg_time','last_ip']
    readonly_fields=['pwd','salt']

admin.site.register(Account,AccountAdmin)
