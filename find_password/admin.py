from django.contrib import admin
from .models import FindPassword


class FindPasswordAdmin(admin.ModelAdmin):
    list_display = ['id', 'account','email', 'date_time', 'valid', 'key']


admin.site.register(FindPassword, FindPasswordAdmin)
