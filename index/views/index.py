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
from feedback.models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from .func import *
from .publish_func import *
from django.db.models import Q 
from django.utils import timezone
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings


# Close csrf validate temporarily
@csrf_exempt
def feedback_service(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None
    content = request.POST.get('content', '')
    if not content or len(content)>500:
        return HttpResponse('false')
    
    feedback = Feedback(user=user,user_content=content)
    feedback.save()

    return HttpResponse('true')


# Close csrf validate temporarily
@csrf_exempt
def item_edit_service(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None
    if not user:
        return HttpResponse('false')

    pid = request.POST.get('pid', '')
    name = request.POST.get('name', '')
    purpose = request.POST.get('purpose', '')
    category = request.POST.get('category', '')
    price = request.POST.get('price', 0)
    condition = request.POST.get('condition', '')
    phone = request.POST.get('phone', '')
    qq = request.POST.get('qq', '')
    campus = request.POST.get('campus', '')
    content = request.POST.get('content', '')
    files = request.FILES
    file_list = list(request.FILES.keys())

    try:
        product = Product.objects.get(id=pid)
        if not product.owner==user:
            return HttpResponse('false')
    except:
        return HttpResponse('false')

    validate_success = validate_publish(name, purpose, category, price, condition,
                     phone, qq, campus, content, files)

    if not validate_success:
        return HttpResponse('false')

    # Get big_imgs and small_imgs
    big_imgs, small_imgs = build_big_imgs_and_small_imgs(files)

    # Save imgs
    save_big_and_small_files(big_imgs, small_imgs, files)
    
    product = Product(id=product.id, name=name, purpose=purpose, category=category, price=price,
                      condition=condition, phone=phone, qq=qq, campus=campus,
                      content=content, big_imgs=big_imgs, small_imgs=small_imgs,
                      owner=user)
    product.save()

    return HttpResponse('true')

# Close csrf validate temporarily
@csrf_exempt
def publish_want_service(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None
    if not user:
        return HttpResponse('false')

    name = request.POST.get('name', '')
    purpose = '3'
    category = request.POST.get('category', '')
    price = request.POST.get('price', '')
    condition = '0'
    phone = request.POST.get('phone', '')
    qq = request.POST.get('qq', '')
    campus = request.POST.get('campus', '')
    content = request.POST.get('content', '')

    validate_success = validate_publish(name, purpose, category, price, condition,
                     phone, qq, campus, content, '','want')
    if not validate_success:
        return HttpResponse('false')

    big_imgs = 'big/big_default_want.jpg'
    small_imgs = 'small/small_default_want.jpg'
    product = Product(name=name, purpose=purpose, category=category, price=price,
                      condition=condition, phone=phone, qq=qq, campus=campus,
                      content=content, big_imgs=big_imgs, small_imgs=small_imgs,
                      owner=user)
    product.save()
    return HttpResponse('true')

# Close csrf validate temporarily
@csrf_exempt
def publish_sale_service(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None
    if not user:
        return HttpResponse('false')

    name = request.POST.get('name', '')
    purpose = request.POST.get('purpose', '')
    category = request.POST.get('category', '')
    price = request.POST.get('price', 0)
    condition = request.POST.get('condition', '')
    phone = request.POST.get('phone', '')
    qq = request.POST.get('qq', '')
    campus = request.POST.get('campus', '')
    content = request.POST.get('content', '')
    files = request.FILES
    file_list = list(request.FILES.keys())

    validate_success = validate_publish(name, purpose, category, price, condition,
                     phone, qq, campus, content, files)

    if not validate_success:
        return HttpResponse('false')

    # Get big_imgs and small_imgs
    big_imgs, small_imgs = build_big_imgs_and_small_imgs(files)

    # Save imgs
    save_big_and_small_files(big_imgs, small_imgs, files)
    
    product = Product(name=name, purpose=purpose, category=category, price=price,
                      condition=condition, phone=phone, qq=qq, campus=campus,
                      content=content, big_imgs=big_imgs, small_imgs=small_imgs,
                      owner=user)
    product.save()

    return HttpResponse('true')


# Close csrf validate temporarily
@csrf_exempt
def comment_service(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None
    if not user:
        return HttpResponse('false')
    comment = request.POST.get('comment', '')
    pid = request.POST.get('pid', False)

    try:
        product = Product.objects.get(id=pid)
        comment_obj = Comment(comment_from=user, product=product, content=comment)
        comment_obj.save()
    except:
        return HttpResponse('false')

    return HttpResponse('true')


def reset_password(request):
    key = None
    try:
        key = request.GET['key']
    except KeyError:
        key = None
    
    email = None
    date_time = None
    try:
        find_password_obj = FindPassword.objects.get(key=key)
        email = find_password_obj.email
        date_time = find_password_obj.date_time
        is_link_valid = find_password_obj.valid

        # Reset link is valid within 30 mins      
        now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
        if (now - date_time).seconds>1800:
            find_password_obj.valid = False
            key = None
        if not is_link_valid:
            key = None

    except:
        key = None

    return render(request, 'reset_password.html', {'key': key})


def find_password(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None

    return render(request, 'find_password.html', {'user': user})



def sign_complete(request):
    user = None
    try:
        user = Account.objects.get(id=request.session['user_id'])
    except:
        user = None
    return render(request, 'sign_complete.html', {'user': user} )


# Close csrf validate temporarily
@csrf_exempt
def index(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None

    # Get notice
    notice = None
    try:
        notice = Notice.objects.filter(valid=True)[0]
    except:
        notice = None

    category = 'new'
    try:
        category = request.GET['category']
        if not category in ['new', 'hot', 'change', 'want']:
            category = 'new'
    except:
        category = 'new'

    page = 1
    max_page_num = max_page(category)
    max_page_num = max_page_num if max_page_num != 0 else 1
    try:
        page = request.GET['page']
        page = int(page)
        page = page if page >= 1 else 1
        page = page if page <= max_page_num else max_page_num
    except:
        page = 1

    items = page_items(category, page)


    if max_page_num <= 5:
        start_page = 1
        end_page = max_page_num
    else:
        if page <= 3:
            start_page = 1
            end_page = 5
        else:
            start_page = page - 2
            end_page = page + 2 if page + 2 <= max_page_num else max_page_num

    render_dic = {
            'user': user,
            'items': items,
            'request': request,
            'notice': notice,
            'category': category,
            'current_page': page,
            'page_range': range(start_page, end_page+1),
            'max_page': max_page_num,
    }
    return render(request, "index.html", render_dic )

# Search result page, keyword conveyed by GET method
def search(request):
    # Get logined user for rendering header
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None

    keyword = ''
    try:
        keyword = request.GET['keyword']
    except KeyError:
        keyword = ''

    # Search result exclude invalid products
    result_list = Product.objects.filter(valid=True).filter(deleted=False).filter(Q(name__icontains=keyword) |
                                                            Q(owner__name__icontains=keyword) |
                                                            Q(content__icontains=keyword)).order_by('pub_date')

    campus = request.GET.get('campus', False)
    category = request.GET.get('category', False)

    if not campus in ['NQ','NL','NH','XM','CY','HP']:
        campus = 'all'

    if not category in ['DB', 'SM', 'DQ', 'WT', 'FS', 'XL', 'ZS', 'XN', 'RY', 'SK', 'SP', 'QT']:
        category = 'all'

    render_dict = {
            'user': user,
            'items': result_list,
            'keyword': keyword,
            'campus': campus,
            'category': category,
    }

    return render(request, "search.html", render_dict)


def detail(request):
    # Get logined user for rendering header
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None

    pid = request.GET.get('pid', False)
    item = None
    try:
        item = Product.objects.get(id=pid)
    except:
        item = None
    if item==None:
        raise Http404('Wrong URL')
    # Add related product's visitors field
    item.visitors += 1
    item.save()

    recommand_item = Product.objects.filter(valid=True).filter(deleted=False)
    recommand_item = recommand_item.filter(category=item.category).order_by('pub_date')
    try:
        recommand_item = recommand_item[0]
    except:
        recommand_item = None

    # Comments
    comments = []
    comments = Comment.objects.filter(valid=True)
    comments = comments.filter(product=item).order_by('pub_date')

    render_dict = {
            'user': user,
            'item': item,
            'small_imgs': item.small_imgs.split(';'),
            'big_imgs': item.big_imgs.split(';'),
            'recommand_item': recommand_item,
            'comments': comments,
    }
    return render(request, "detail.html", render_dict )

def publish(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None

    # Get action to detect either want or sell
    action = ''
    is_want = False
    try:
        action = request.GET['action']
        if action == 'want':
            is_want = True
        else:
            is_want = False
    except KeyError:
        is_want = False


    render_dict = {
            'user': user,
            'is_want': is_want,
    }
    return render(request, "publish.html", render_dict)


def item_edit(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None
    pid = request.GET.get('pid', '')
    item = ''
    try:
        item = Product.objects.get(id=pid)
    except:
        item = ''
    return render(request, "item-edit.html", {'user': user, 'item': item} )


def account(request, frame):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None

    return render(request, "account.html", {'user': user, 'frame_url':frame})

def ucenter(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None

    account_id = request.GET.get('uid', False)
    try:
        account = Account.objects.get(id=account_id)
    except:
        account = None

    try:
        items = Product.objects.filter(owner=account).filter(valid=True).order_by('-pub_date')
    except:
        items = None

    return render(request, "ucenter.html", {'user': user, 'account': account, 'items':items} )


def pub_success(request):
    return HttpResponse('Publish Success Page Here.')


def register(request):
    return HttpResponse('Register Page Here.')


def reg_success(request):
    return HttpResponse('Register Success Page Here.')


def about(request):
    # Get logined user for rendering header
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except:
        user = None

    label = request.GET.get('label', 'help')
    if not label in ['help', 'about', 'contact', 'recruit', 'cooperation', 'feedback']:
        label = 'help'

    # Get feedback
    feedback = Feedback.objects.filter(valid=True).order_by('-admin_pub_date', '-user_pub_date')

    return render(request, 'about.html', {'user': user, 'label': label, 'feedback': feedback})
