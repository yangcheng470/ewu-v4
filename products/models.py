from django.db import models
from django.utils import timezone


class Product(models.Model):
    name=models.CharField(max_length=200,null=False)
    
    CATEGORY_CHOICES=(
            ('DB','代步'),
            ('DQ','电器'),
            ('FS','服饰'),
            ('XL','鞋履'),
            ('XN','虚拟'),
            ('SP','食品'),
            ('SM','数码'),
            ('WT','文体'),
            ('SK','书刊'),
            ('ZS','装饰'),
            ('RY','日用'),
            ('QT','其他'),
    )
    category=models.CharField(max_length=2,
                              null=False,
                              choices=CATEGORY_CHOICES,
                              default='QT'
    )

    # Most 7 digits, with 2 decimals, for instance, 45.98
    price=models.DecimalField(max_digits=7,decimal_places=2,default=0) 

    # Condition of the product, with one decimal and most two integer
    # For instance, 9.8    10.0
    condition=models.DecimalField(max_digits=3,
                                  decimal_places=1,
                                  default=0.0)     
    owner=models.ForeignKey('accounts.Account')

    # S for sale, E for exchange
    # This is function is to be done
    # status=models.CharField(max_length=1,default='S')  

    # Most 5 imgs, file name split with ':'
    imgs=models.CharField(max_length=200)  

    content=models.TextField()

    pub_date=models.DateTimeField(default=timezone.now)

    # If sold, valid field can be set to False
    valid=models.BooleanField(default=True)

    # return content for admin interface
    def get_content(self):
        if len(self.content)>80:
            return self.content[:77]+' ...'
        else:
            return self.content

    get_content.short_description='Content'

    def __str__(self):
        return self.name
