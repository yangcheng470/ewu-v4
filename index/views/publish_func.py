import re
import datetime
import pytz
import time
from hashlib import md5
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from accounts.models import Account
from products.models import Product
from comments.models import Comment
from notice.models import Notice
from find_password.models import FindPassword
from django.views.decorators.csrf import csrf_exempt
from .func import *


def validate_publish(name, purpose, category, price, condition,
                     phone, qq, campus, content, files, type="sale"):

    if (not re.match(r'^.{2,100}$', name) or
        not purpose in ['1', '2', '3'] or
        not category in ['DB', 'SM', 'DQ', 'WT', 'FS', 'XL', 'ZS', 'XN', 'RY', 'SK', 'SP', 'QT'] or
        not re.match(r'^[0-9.]{1,10}$', price) or
        not re.match(r'^[0-9]$', condition) or
        not campus in ['NQ','NL','NH','XM','CY','HP'] or
        not re.match(r'^.{2,500}$', content)):
            return False

    # If validate 'want' type, that's enough
    if type == 'want' and purpose == '3':
        return True

    if not (len(files)>0 and len(files)<5):
        return False

    # Check imgs' size, less than 10M(10240K)
    for file_obj in files.values():
        if file_obj.size>10240*1024:
            return False

    # Check if is imgs through suffix
    valid_suffix = ['jpg', 'png', 'bmp', 'jpeg']
    for file_obj in files.values():
        suffix = file_obj.name.split('.')[-1].lower()
        if not suffix in valid_suffix:
            return False

    return True


# Build big_imgs and small_imgs, seperate path with ';'
def build_big_imgs_and_small_imgs(files):
    big_imgs = ''
    small_imgs = ''
    for file_obj in files.values():
        # Get suffix
        suffix = file_obj.name.split('.')[-1]
        # Get file name, no suffix
        file_name = file_obj.name

        # Build file name with some random chars as a partion
        # Add timestamp
        file_name += str(time.time())

        file_name = md5(file_name.encode()).hexdigest() + '.' + suffix
        big_imgs += 'big/big_' + file_name + ';'
        small_imgs += 'small/small_' + file_name + ';'

    # Remove last ';'
    if big_imgs[-1] == ';':
        big_imgs = big_imgs[:-1]
        small_imgs = small_imgs[:-1]

    return (big_imgs, small_imgs)


# Write big and small files to hard disk
def save_big_and_small_files(big_imgs, small_imgs, files):
    big_imgs = big_imgs.split(';')
    small_imgs = small_imgs.split(';')
    i = 0;
    for file_obj in files.values():
        with open('media/' + big_imgs[i], 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        with open('media/' + small_imgs[i], 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        i += 1
    return True
