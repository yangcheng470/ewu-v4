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

    PURPOSE_CHOICES = (
            ('1', '出售'),
            ('2', '交换'),
            ('3', '求购'),
    )
    purpose = models.CharField(max_length=1, choices=PURPOSE_CHOICES, default='1')

    CAMPUS_CHOICES = (
            ('NQ', '南区'),
            ('HP', '和平'),
            ('CY', '朝阳'),
            ('XM', '新民'),
            ('NH', '南湖'),
            ('NL', '南岭'),
    )
    campus = models.CharField(max_length=2,
                              null=False,
                              choices=CAMPUS_CHOICES,
                              default='NQ'
    )


    # Most 7 digits, with 2 decimals, for instance, 45.98
    price=models.DecimalField(max_digits=7,decimal_places=2,default=0) 

    # Condition of the product, with one decimal and most two integer
    # For instance, 9.8    10.0
    condition=models.DecimalField(max_digits=3,
                                  decimal_places=1,
                                  default=0.0)     
    owner=models.ForeignKey('accounts.Account')

    # This field has magnitude sale < sold
    STATUS_CHOICES = (
            ('sale', '在售'),
            ('sold', '已售'),
    )
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='sale')

    deleted = models.BooleanField(default=False)

    small_imgs = models.ImageField(upload_to='small', default='small/default.png')
    big_imgs = models.ImageField(upload_to='big', default='big/default.png')
    # Below two fields are out of convenient
    small_img = models.CharField(max_length=500)
    big_img = models.CharField(max_length=500)

    content=models.TextField()

    pub_date=models.DateTimeField(default=timezone.now)

    # If sold or other reason, valid field will be set to False
    valid=models.BooleanField(default=True)

    visitors=models.PositiveIntegerField(default=0)

    # Return content for admin interface
    # If content's length is greater than 80,
    # only 77 chars will be displayed together with "..."
    def get_content(self):
        if len(self.content)>80:
            return self.content[:77]+' ...'
        else:
            return self.content

    get_content.short_description='Content'

    # Rewrite save method to auto assign values to small_img and big_img
    def save(self, *args, **kwargs):
        self.small_img = str(self.small_imgs).split(';')[0]
        self.big_img = str(self.big_imgs).split(';')[0]

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
