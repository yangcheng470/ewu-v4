from django.db import models

# Create your models here.


class Account(models.Model):
    name=models.CharField(max_length=50,null=False)
    sex=models.CharField(max_length=1,null=False)  # m for male, f for female
    pwd=models.CharField(max_length=64,null=False)
    salt=models.CharField(max_length=64,null=False)
    email=models.EmailField(null=False)
    email_verified=models.BooleanField(default=False)
    phone=models.CharField(max_length=11) 
    phone_verified=models.BooleanField(default=False)
    reg_time=models.DateTimeField(null=True)
    last_ip=models.GenericIPAddressField(null=True)

    CAMPUS_CHOICES=(
            ('NQ','南区'),
            ('NL','南岭'),
            ('NH','南湖'),
            ('HP','和平'),
            ('CY','朝阳'),
            ('XM','新民'),
    )
    campus=models.CharField(max_length=2,choices=CAMPUS_CHOICES,default='NQ')

    def __str__(self):
        return self.name
