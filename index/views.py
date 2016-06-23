from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from accounts.models import Account
from products.models import Product


def index(request):
    user_id = request.session.get('user_id', False)
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        user = None
    items = Product.objects.order_by('pub_date').filter(valid=True)
    return render(request, "index.html", {'user': user, 'items': items })

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
    return render(request, "account.html", {})

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
