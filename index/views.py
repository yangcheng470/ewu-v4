import logging
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from accounts.models import Account
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from .func import *

logger = logging.getLogger(__name__)                                                 
logger.setLevel(logging.INFO)
handler = logging.FileHandler('ewu.log')
formatter = logging.Formatter('[%(asctime)s]-%(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


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
        except Account.DoesNotExist:
            pass

        salt = generate_salt()
        encrypted_password = encrypt_pwd(password, salt)
        user = Account(name=name, email=email, pwd=encrypted_password, salt=salt, last_ip=request.META['REMOTE_ADDR'])
        user.save()
        request.session['user_id'] = user.id
        return HttpResponse('true')
    except MultiValueDictKeyError:
        return HttpResponse('false')
        

def logout_service(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'logout.html', {'request': request})

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

        salt = user.salt
        # If password is wrong
        if not (encrypt_pwd(password, salt) == user.pwd):
            raise Account.DoesNotExist

        # Save current ip to last_ip field
        user.last_ip = request.META['REMOTE_ADDR']
        user.save()

        request.session['user_id'] = user.id

        return HttpResponse('true')

    except (MultiValueDictKeyError,Account.DoesNotExist):
        return HttpResponse('false')

    

def index(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None
    items = Product.objects.order_by('pub_date').filter(valid=True)
    return render(request, "index.html", {'user': user, 'items': items, 'request': request })

# Search result page, keyword conveyed by GET method
def search(request):
    return render(request, "search.html", {})

def detail(request):
    pid = request.GET.get('pid', False)
    item = None
    try:
        item = Product.objects.get(id=pid)
    except Product.DoesNotExist:
        item = None
    if item==None:
        raise Http404('Wrong URL')
    small_imgs = str(item.small_imgs).split(':')
    big_imgs = str(item.big_imgs).split(':')
    recommand_item = Product.objects.filter(category=item.category).order_by('pub_date')[0]
    return render(request, "detail.html", {'item': item, 'small_imgs': small_imgs, 'big_imgs': big_imgs, 'recommand_item': recommand_item })

def publish(request):
    return render(request, "publish.html", {})

def my_items(request):
    return render(request, "my-items.html", {})

def item_edit(request):
    return render(request, "item-edit.html", {})

def messages(request):
    return render(request, "msg.html", {})

def account(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None

    return render(request, "account.html", {'user': user})

def ucenter(request):
    return render(request, "ucenter.html", {})

def change_password(request):
    return render(request, "change-password.html", {})

def pub_success(request):
    return HttpResponse('Publish Success Page Here.')


def register(request):
    return HttpResponse('Register Page Here.')


def reg_success(request):
    return HttpResponse('Register Success Page Here.')

def help(request):
    return HttpResponse('Help Page Here.')


def about(request):
    return HttpResponse('About Page Here.')
