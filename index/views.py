from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Index Page Here.')


def publish(request):
    return HttpResponse('Publish Page Here.')


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
