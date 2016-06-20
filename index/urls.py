from django.conf.urls import url,include
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^search/$',views.search,name='search'),
        url(r'^detail/', views.detail, name='detail'),
        url(r'^publish/$',views.publish,name='publish'),
        url(r'^publish/success/$',views.pub_success,name='pub_success'),
        url(r'^register/$',views.register,name='register'),
        url(r'^register/success/$',views.reg_success,name='reg_success'),
        url(r'^ucenter/', views.ucenter, name='ucenter'),
        url(r'^account/', views.account, name='account'),
        url(r'^help/$',views.help,name='help'),
        url(r'^about/$',views.about,name='about'),
]
