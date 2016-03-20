from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Index Page Here.</h1>')


def help(request):
    return HttpResponse('<h1>help Page Here.</h1>')


def about(request):
    return HttpResponse('<h1>about Page Here.</h1>')
