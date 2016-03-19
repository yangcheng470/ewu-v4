from django.db import models


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

    price=models.PositiveIntegerField(default=0) # Must be positive price

    # Condition of the product, with one decimal and most two integer
    # For instance, 9.8    10.0
    condition=models.DecimalField(max_digits=3,
                                  decimal_places=1,
                                  default=0.0)     
    owner=models.ForeignKey('accounts.Account')

    # S for sale, E for exchange
    status=models.CharField(max_length=1,default='S')  

    # Most 5 imgs, file name split with ':'
    imgs=models.CharField(max_length=200)  

    content=models.TextField()
