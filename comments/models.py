from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    comment_from=models.ForeignKey('accounts.Account',related_name='comment_from')
    comment_to=models.ForeignKey('accounts.Account',related_name='comment_to')
    pub_date=models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=300)

    def __str__(self):
        return self.comment_from
