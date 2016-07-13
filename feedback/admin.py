from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_content', 'user_pub_date', 'admin_content', 'admin_pub_date']


admin.site.register(Feedback,FeedbackAdmin)
