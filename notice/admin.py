from django.contrib import admin
from .models import Notice

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_name', 'title', 'pub_date', '__get_content__']
    list_display_links = ['id', 'title']


admin.site.register(Notice, NoticeAdmin)
