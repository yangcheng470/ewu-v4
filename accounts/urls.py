from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^reset-password/$',views.reset_passwd,name='reset_passwd'),
        url(r'^reset-password/success$',views.reset_passwd_success,name='reset_passwd_success'),
        url(r'^delete-account/$',views.delete_account,name='delete_account'),
        url(r'^delete-account/success/$',views.delete_account_success,name='delete_account_success'),
]
