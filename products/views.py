from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    return HttpResponse('<h1>Product Index Here.</h1>')


def detail(request,product_id):
    try:
        product=Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product does not exist.')
    else:
        return HttpResponse('<h1>Product name: %s. </h1>' % product.name)
