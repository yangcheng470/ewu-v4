from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display=['id','comment_from','product','pub_date','get_content']


admin.site.register(Comment,CommentAdmin)
