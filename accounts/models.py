from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    name=models.CharField(max_length=50,null=False)
    
    SEX_CHOICES=(
            ('M','男'),
            ('F','女'),
            ('U', '未知'),
    )
    sex=models.CharField(max_length=1,choices=SEX_CHOICES,default='U')
    pwd=models.CharField(max_length=128,null=False)
    salt=models.CharField(max_length=64,null=False)
    email=models.EmailField(null=False)
    email_verified=models.BooleanField(default=False)
    phone=models.CharField(max_length=11, blank=True)
    qq = models.CharField(max_length=20, blank=True)
    phone_verified=models.BooleanField(default=False)
    reg_time=models.DateTimeField(default=timezone.now)
    last_ip=models.GenericIPAddressField(null=True)
    visitors=models.PositiveIntegerField(default=0)

    valid = models.BooleanField(default=True)

    CAMPUS_CHOICES=(
            ('NQ','南区'),
            ('NL','南岭'),
            ('NH','南湖'),
            ('HP','和平'),
            ('CY','朝阳'),
            ('XM','新民'),
    )
    campus=models.CharField(max_length=2,choices=CAMPUS_CHOICES,default='NQ')

    college = models.CharField(max_length=30, blank=True)
    entry_year = models.CharField(max_length=4, blank=True)

    def unread_comment_count(self):
        unread_comment_list = self.comment_forward.all()
        # Exclude owner's comments
        unread_comment_list = unread_comment_list.exclude(comment_from=self)
        unread_comment_list = unread_comment_list.filter(valid=True)
        unread_comment_list = unread_comment_list.filter(readed=False)
        return len(unread_comment_list)

    def __str__(self):
        return self.name

