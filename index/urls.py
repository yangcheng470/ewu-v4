from django.conf.urls import url,include
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns=[
        url(r'^$',views.index,name='index'),
        url(r'^search/$',views.search,name='search'),
        url(r'^detail/', views.detail, name='detail'),
        url(r'^publish/$',views.publish,name='publish'),
        url(r'^item-edit/$',views.item_edit,name='item_edit'),
        url(r'^ucenter/', views.ucenter, name='ucenter'),
        url(r'^account/(?P<frame>.*)/$', views.account, name='account'),
        url(r'^help/$',views.help,name='help'),
        url(r'^about/$',views.about,name='about'),
        url(r'^find_password/$',views.find_password, name='find_password'),

        # Account service about
        url(r'^service/login/$', views.login_service, name='login_service'),
        url(r'^service/logout/$', views.logout_service, name='logout_service'),
        url(r'^service/register/$', views.reg_service, name='reg_service'),
        url(r'^service/change-password/$', views.change_pwd_service, name='change_pwd_service'),
        url(r'^service/find_password/$', views.find_password_service, name='find_password_service'),

        # Sign up complete
        url(r'^sign_complete/$', views.sign_complete, name='sign_complete'),

        # Account frames
        url(r'^frames/person_info/$', views.person_info, name='person_info'),
        url(r'^frames/change-password/$', views.change_password, name='change_password'),
        url(r'^frames/messages/$',views.messages,name='messages'),
        url(r'^frames/my-items/$',views.my_items,name='my_items'),
        url(r'^frames/logout/$',views.logout,name='logout'),

        # Account frames for mobile
        url(r'^frames/mobile/person_info/$', views.mobile_person_info, name='mobile_person_info'),
        url(r'^frames/mobile/change-password/$', views.mobile_change_password, name='mobile_change_password'),
        url(r'^frames/mobile/messages/$',views.mobile_messages,name='mobile_messages'),
        url(r'^frames/mobile/my-items/$',views.mobile_my_items,name='mobile_my_items'),
        url(r'^frames/mobile/logout/$',views.mobile_logout,name='mobile_logout'),
]
