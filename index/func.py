#!/usr/bin/env python
import hashlib
import random
from products.models import Product

def generate_salt():
    chars = 'abcdefghijklmnopqrstuvwxyz'
    chars += '0123456789'
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    salt = ''
    for i in range(0, 64):
        index = random.randint(0, len(chars)-1)
        salt += chars[index]

    return salt

def encrypt_pwd(plain_pwd, salt):
    if not len(salt)==64:
        return None
    # First step should be md5 in order to be compatible
    plain_pwd = hashlib.md5(plain_pwd.encode()).hexdigest()
    plain_pwd += salt
    encrypt_pwd = hashlib.sha512(plain_pwd.encode()).hexdigest()
    return encrypt_pwd


def max_items(category='new'):
    if not category in ['new', 'hot', 'change', 'want']:
        category = 'new'

    total_item_num = 0
    if category=='new' or category=='hot':
        total_item_num = Product.objects.filter(valid=True).count()
    elif category == 'change':
        total_item_num = Product.objects.filter(valid=True).filter(purpose='2').count()
    else:
        total_item_num = Product.objects.filter(valid=True).filter(purpose='3').count()
    return total_item_num


def max_page(category='new'):
    if not category in ['new', 'hot', 'change', 'want']:
        category = 'new'

    total_item_num = max_items(category)
    max_page = total_item_num / 20

    if int(max_page)<max_page:
        return int(max_page + 1)
    else:
        return int(max_page)


def page_items(category='new', page=1):
    if not category in ['new', 'hot', 'change', 'want']:
        category = 'new'

    if page<1 or page>max_page():
        page = 1
    
    page_list = []
    if category == 'new':
        page_list = Product.objects.filter(valid=True).order_by('-pub_date')
    elif category == 'hot':
        page_list = Product.objects.filter(valid=True).order_by('-visitors')
    elif category == 'change':
        page_list = Product.objects.filter(valid=True).filter(purpose='2').order_by('-visitors')
    else:
        page_list = Product.objects.filter(valid=True).filter(purpose='3').order_by('-visitors')

    begin = (page-1)*20
    if max_items(category) < page*20:
        end = max_items(category) + 1
    else:
        end = page * 20 + 1
    page_list = page_list[begin:end]

    return page_list


if __name__ == '__main__':
    salt = generate_salt()
    print(salt)
    print(encrypt_pwd('hello', salt))
    print(max_page())
