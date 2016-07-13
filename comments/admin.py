from django.contrib import admin
from .models import Comment

# Register your models here.

def set_invalid(modeladmin, request, queryset):
    queryset.update(valid=False)

set_invalid.short_description = "设置为无效"


class CommentAdmin(admin.ModelAdmin):
    list_display=['id','comment_from','product','pub_date','get_content', 'valid']
    ordering=['id']
    actions = [set_invalid]


admin.site.register(Comment,CommentAdmin)
