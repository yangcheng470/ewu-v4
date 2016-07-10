from django.db import models
from accounts.models import Account
from django.utils import timezone


class FindPassword(models.Model):
    account = models.OneToOneField(Account)
    email=models.EmailField(null=False)
    date_time = models.DateTimeField(default=timezone.now)
    valid = models.BooleanField(default=False)
    key = models.CharField(max_length=64)

    def __str__(self):
        return self.account.name
