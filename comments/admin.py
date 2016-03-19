from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display=['comment_from','comment_to','pub_date','get_content']


admin.site.register(Comment,CommentAdmin)
