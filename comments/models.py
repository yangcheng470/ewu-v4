from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    comment_from=models.ForeignKey('accounts.Account',related_name='comment_from')
    comment_to=models.ForeignKey('accounts.Account',related_name='comment_to')
    pub_date=models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=300)

    def get_content(self):
        if len(self.content)>80:
            return self.contene[:77]+' ...'
        else:
            return self.content

    get_content.short_description='Comment contene'

    def __str__(self):
        return self.content
