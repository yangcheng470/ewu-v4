from django.conf.urls import url,include
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^search/$',views.search,name='search'),
        url(r'^detail/', views.detail, name='detail'),
        url(r'^publish/$',views.publish,name='publish'),
        url(r'^my-items/$',views.my_items,name='my_items'),
        url(r'^item-edit/$',views.item_edit,name='item_edit'),
        url(r'^messages/$',views.messages,name='messages'),
        url(r'^ucenter/', views.ucenter, name='ucenter'),
        url(r'^account/', views.account, name='account'),
        url(r'^change-password/', views.change_password, name='change_password'),
        url(r'^help/$',views.help,name='help'),
        url(r'^about/$',views.about,name='about'),
        # Login about
        url(r'^service/login/$', views.login_service, name='login_service'),
        url(r'^service/logout/$', views.logout_service, name='logout_service'),
        url(r'^service/register/$', views.reg_service, name='reg_service'),
]
