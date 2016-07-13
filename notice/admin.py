from django.contrib import admin
from .models import Notice

# Register your models here.

def set_as_current_notice(modeladmin, request, queryset):
    if not len(queryset)==1:
        return False
    Notice.objects.all().update(valid=False)
    queryset.update(valid=True)

set_as_current_notice.short_description = '设为当前公告'


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'valid', 'pub_name', 'title', 'pub_date', '__get_content__']
    list_display_links = ['id', 'title']
    readonly_fields = ['valid']
    actions = [set_as_current_notice]


admin.site.register(Notice, NoticeAdmin)
