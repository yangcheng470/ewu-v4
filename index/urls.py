from django.conf.urls import url,include
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^search/$',views.search,name='search'),
        url(r'^detail/', views.detail, name='detail'),
        url(r'^publish/$',views.publish,name='publish'),
        url(r'^messages/$',views.messages,name='messages'),
        url(r'^ucenter/', views.ucenter, name='ucenter'),
        url(r'^account/', views.account, name='account'),
        url(r'^change-password/', views.change_password, name='change-password'),
        url(r'^help/$',views.help,name='help'),
        url(r'^about/$',views.about,name='about'),
]
