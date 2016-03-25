from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Ucenter page here.')


def reset_passwd(request):
    return HttpResponse('Reset password page here.')


def reset_passwd_success(request):
    return HttpResponse('Reset password success page here.')
