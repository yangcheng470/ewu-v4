from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    comment_from = models.ForeignKey('accounts.Account', related_name='comment_from', null=True)
    comment_forward = models.ForeignKey('accounts.Account', related_name='comment_forward', null=True)
    product=models.ForeignKey('products.Product',null=True)
    pub_date=models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=300)

    readed = models.BooleanField(default=False)

    valid = models.BooleanField(default=True)

    def get_content(self):
        if len(self.content)>80:
            return self.content[:77]+' ...'
        else:
            return self.content

    get_content.short_description='Comment content'

    def __str__(self):
        return self.content

    # Auto fill comment_forward field according to product
    def save(self, *args, **kwargs):
        product_owner = self.product.owner
        self.comment_forward = product_owner

        super(Comment, self).save(*args, **kwargs)
