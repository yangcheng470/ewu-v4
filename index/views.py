import logging
import re
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


def find_password(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'find_password.html', {'user': user})


@csrf_exempt
def find_password_service(request):
    logger.info('asdasd')
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
    except Account.DoesNotExist:
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
    except FindPassword.DoesNotExist:
        find_password_obj = FindPassword(account=user, date_time=timezone.now(),valid=True, key=key, email=email)
    find_password_obj.save()
    
    # Construct a find_password url
    url = "http://www.jluewu.com/service/reset_password/?key=" + key

    # Start render mail template
    mail = loader.render_to_string('find_password_mail.html', {'url': url})
    send_mail('吉大易物-找回密码','','admin', [email], fail_silently=True, html_message=mail)
    return HttpResponse('true')


def sign_complete(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None
    return render(request, 'sign_complete.html', {'user': user} )

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


# Mobile

def mobile_person_info(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/mobile/person_info.html', {'user': user})


def mobile_change_password(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/mobile/change_password.html', {'user': user})


def mobile_messages(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/mobile/messages.html', {'user': user})


def mobile_my_items(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/mobile/my_items.html', {'user': user})


def mobile_logout(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except (Account.DoesNotExist, KeyError):
        user = None

    return render(request, 'frames/mobile/logout.html', {'user': user})


# Close csrf validate temporarily
@csrf_exempt
def change_pwd_service(request):
    if request.method == 'GET':
        raise Http404('Wrong url')

    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except Account.DoesNotExist:
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
    return HttpResponse('true')

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

    # Get notice
    notice = None
    try:
        notice = Notice.objects.order_by('-pub_date')[0]
    except:
        notice = None
    return render(request, "index.html", {'user': user, 'items': items, 'request': request, 'notice': notice} )

# Search result page, keyword conveyed by GET method
def search(request):
    # Get logined user for rendering header
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None

    keyword = ''
    try:
        keyword = request.GET['keyword']
    except KeyError:
        keyword = ''

    if not keyword:
        return render(request, "search.html", {'user': user, 'items': []} )
    
    # Search result exclude invalid products
    result_list = Product.objects.filter(valid=True).filter(Q(name__icontains=keyword) or
                                                            Q(owner__icontains==keyword) or
                                                            Q(content__icontains=keyword)).order_by('pub_date')


    return render(request, "search.html", {'user': user, 'items': result_list, 'keyword': keyword})


def detail(request):
    # Get logined user for rendering header
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None

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
    render_dic = {
            'user': user,
            'item': item,
            'small_imgs': small_imgs,
            'big_imgs': big_imgs,
            'recommand_item': recommand_item,
    }
    return render(request, "detail.html", render_dic )

def publish(request):
    # Get action to detect either want or sell
    action = ''
    try:
        action = request.GET['action']
    except KeyError:
        action = ''

    if action=='want':
        return render(request, "publish.html", {'is_want':True})
    else:
        return render(request, "publish.html", {'is_want':False})


def item_edit(request):
    return render(request, "item-edit.html", {})


def account(request, frame):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None

    return render(request, "account.html", {'user': user, 'frame_url':frame})

def ucenter(request):
    return render(request, "ucenter.html", {})


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
