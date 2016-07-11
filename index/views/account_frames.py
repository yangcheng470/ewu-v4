import logging
import re
import datetime
import pytz
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from accounts.models import Account
from products.models import Product
from notice.models import Notice
from find_password.models import FindPassword
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from .func import *
from django.db.models import Q 
from django.utils import timezone
from django.core.mail import send_mail
from django.template import loader

logger = logging.getLogger(__name__)                                                 
logger.setLevel(logging.INFO)
handler = logging.FileHandler('ewu.log')
formatter = logging.Formatter('[%(asctime)s]-%(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def person_info(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/person_info.html', {'user': user})


def change_password(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/change_password.html', {'user': user})


def messages(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/messages.html', {'user': user})


def my_items(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/my_items.html', {'user': user})


def logout(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/logout.html', {'user': user})

