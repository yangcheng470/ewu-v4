from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    comment_from=models.ForeignKey('accounts.Account')
    product=models.ForeignKey('products.Product',null=True)
    pub_date=models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=300)

    readed = models.BooleanField(default=False)

    valid = models.BooleanField(default=True)

    def get_content(self):
        if len(self.content)>80:
            return self.contene[:77]+' ...'
        else:
            return self.content

    get_content.short_description='Comment contene'

    def __str__(self):
        return self.content
