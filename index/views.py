from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request, "detail.html", {})

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
