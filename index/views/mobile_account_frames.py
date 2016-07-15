import re
import datetime
import pytz
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from accounts.models import Account
from products.models import Product
from notice.models import Notice
from comments.models import Comment
from find_password.models import FindPassword
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from .func import *
from django.db.models import Q
from django.utils import timezone
from django.core.mail import send_mail
from django.template import loader


def mobile_person_info(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    return render(request, 'frames/mobile/person_info.html', {'user': user})


def mobile_change_password(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    return render(request, 'frames/mobile/change_password.html', {'user': user})


def mobile_messages(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    messages = Comment.objects.filter(valid=True)
    messages = messages.filter(comment_forward=user).order_by('readed', '-pub_date')

    # copy_messages is for update readed status
    # convert messages to list is to query last status
    copy_messages = messages
    messages = list(messages)
    copy_messages.update(readed=True)

    return render(request, 'frames/mobile/messages.html', {'user': user, 'messages': messages})


def mobile_my_items(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    items = Product.objects.filter(valid=True).filter(deleted=False)
    items = items.filter(owner=user)

    return render(request, 'frames/mobile/my_items.html', {'user': user, 'items': items})


def mobile_logout(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    return render(request, 'frames/mobile/logout.html', {'user': user})

