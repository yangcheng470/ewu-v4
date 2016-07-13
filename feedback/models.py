from django.db import models
from django.utils import timezone

# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey('accounts.Account', related_name='user', null=True, blank=True)
    user_content = models.CharField(max_length=300)
    user_pub_date = models.DateTimeField(default=timezone.now)

    admin_content = models.CharField(max_length=300,default='', blank=True)
    admin_pub_date = models.DateTimeField(default=timezone.now)

    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.user_content
