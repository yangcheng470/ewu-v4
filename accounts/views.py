from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Ucenter page here.')


def reset_passwd(request):
    return HttpResponse('Reset password page here.')


def reset_passwd_success(request):
    return HttpResponse('Reset password success page here.')


def delete_account(request):
    return HttpResponse('Delete account page here.')


# Attention: This action is dangerous. Action should be verified by authorizing password.
# After delete account, all relative products should be removed, too.
# All data will be deleted from database physically.
# Why this action is provided? This is a problem just in China, not in foreign.
# This should be the necessary and basic( rather extra ) right.
def delete_account_success(request):
    return HttpResponse('Delete account success page here.')
