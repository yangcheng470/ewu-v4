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


# Close csrf validate temporarily
@csrf_exempt
def login_service(request):
    if request.method == 'GET':
        raise Http404('Wrong URL')

    try:
        email = request.POST['account']
        password = request.POST['password']
        # Validate account and password's length
        if not email or not password:
            raise MultiValueDictKeyError

        # If not exist, Account.DoesNotExist will be raised
        user = Account.objects.get(email=email)

        if not user.valid:
            raise Account.DoesNotExist

        salt = user.salt
        # If password is wrong
        if not (encrypt_pwd(password, salt) == user.pwd):
            raise Account.DoesNotExist

        # Save current ip to last_ip field
        user.last_ip = request.META['REMOTE_ADDR']
        user.save()

        request.session['user_id'] = user.id

        return HttpResponse('true')

    except:
        return HttpResponse('false')

    
def logout_service(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse('true')


# Close csrf validate temporarily
@csrf_exempt
def reg_service(request):
    if request.method == 'GET':
        raise Http404('Wrong URL')

    try:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if not (re.match(r'^.{2,15}$', name) or
                re.match(r'^[a-zA-Z0-9.-_]{2,50}@[a-zA-Z0-9]{2,30}.[a-zA-Z0-9]{1,10}$', email) or
                re.match(r'^.{6,20}$', password)):
            return HttpResponse('false')
        
        try:
            # If email has been registered, return 'register'
            # Or continue
            if Account.objects.get(email=email):
                return HttpResponse('registered')
        except:
            pass

        salt = generate_salt()
        encrypted_password = encrypt_pwd(password, salt)
        user = Account(name=name, email=email, pwd=encrypted_password, salt=salt, last_ip=request.META['REMOTE_ADDR'])
        user.save()
        request.session['user_id'] = user.id
        return HttpResponse('true')
    except:
        return HttpResponse('false')
        

# Close csrf validate temporarily
@csrf_exempt
def change_pwd_service(request):
    if request.method == 'GET':
        raise Http404('Wrong url')

    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    if not user:
        return HttpResponse('false')

    try:
        old_pwd = request.POST['old_pwd']
        new_pwd = request.POST['new_pwd']

        salt = user.salt

        # If password is not correct
        if not encrypt_pwd(old_pwd, salt) == user.pwd:
            return HttpResponse('false')

        # If new password is not suitable
        if not re.match(r'^.{6,20}$', new_pwd):
            return HttpResponse('false')

        # Save new password
        user.pwd = encrypt_pwd(new_pwd, salt)
        user.save()

    except:
        return HttpResponse('false')

    return HttpResponse('true')


@csrf_exempt
def find_password_service(request):
    email = ''
    try:
        email = request.POST['email']
    except:
        email = ''

    if not re.match(r'^[a-zA-Z0-9.-_]{2,50}@[a-zA-Z0-9]{2,30}.[a-zA-Z0-9]{1,10}$', email):
        return HttpResponse('false')

    user = None
    try:
        user = Account.objects.get(email=email)
    except:
        user = None

    if not user:
        return HttpResponse('false')

    key = generate_salt()
    try:
        find_password_obj = FindPassword.objects.get(account=user)
        find_password_obj.email = email
        find_password_obj.date_time = timezone.now()
        find_password_obj.valid = True
        find_password_obj.key = key
    except:
        find_password_obj = FindPassword(account=user, date_time=timezone.now(),valid=True, key=key, email=email)
    find_password_obj.save()
    
    # Construct a find_password url
    url = "http://127.0.0.1:8000/reset_password/?key=" + key

    # Start render mail template
    mail = loader.render_to_string('find_password_mail.html', {'url': url})
    try:
        send_mail('吉大易物-找回密码','','admin', [email],  html_message=mail)
    except:
        return HttpResponse('service_false')
    return HttpResponse('true')


@csrf_exempt
def reset_password_service(request):
    key = None
    password = None
    try:
        key = request.POST['key']
        password = request.POST['password']
    except KeyError:
        return HttpResponse('false')

    try:
        find_password_obj = FindPassword.objects.get(key=key)
        account = find_password_obj.account

        salt = generate_salt()
        account.pwd = encrypt_pwd(password, salt)
        account.salt = salt
        account.save()
        find_password_obj.valid = False
        find_password_obj.save()
        return HttpResponse('true')
    except:
        return HttpResponse('false')


