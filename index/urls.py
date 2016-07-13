from django.conf.urls import url,include
from django.conf import settings
from django.views.static import serve
from index.views import index, account_service
from index.views import account_frames,mobile_account_frames


urlpatterns=[
        url(r'^$',index.index,name='index'),
        url(r'^search/$',index.search,name='search'),
        url(r'^detail/', index.detail, name='detail'),
        url(r'^publish/$',index.publish,name='publish'),
        url(r'^item-edit/$',index.item_edit,name='item_edit'),
        url(r'^ucenter/', index.ucenter, name='ucenter'),
        url(r'^account/(?P<frame>.*)/$', index.account, name='account'),
        url(r'^about/$',index.about,name='about'),
        url(r'^find_password/$',index.find_password, name='find_password'),
        url(r'^reset_password/$', index.reset_password, name='reset_password'),

        # Comment service
        url(r'^service/comment/$', index.comment_service, name='comment_service'),
        # Publish service
        url(r'^service/publish/sale/$', index.publish_sale_service, name='publish_sale_service'),
        url(r'^service/publish/want/$', index.publish_want_service, name='publish_want_service'),

        url(r'^service/item-edit/$', index.item_edit_service, name='item_edit_service'),


        # Account service about
        url(r'^service/login/$', account_service.login_service, name='login_service'),
        url(r'^service/logout/$', account_service.logout_service, name='logout_service'),
        url(r'^service/register/$', account_service.reg_service, name='reg_service'),
        url(r'^service/change-password/$', account_service.change_pwd_service, name='change_pwd_service'),
        url(r'^service/find_password/$', account_service.find_password_service, name='find_password_service'),
        url(r'^service/reset_password/$', account_service.reset_password_service, name='reset_password_service'),

        # Sign up complete
        url(r'^sign_complete/$', index.sign_complete, name='sign_complete'),

        # Account frames
        url(r'^frames/person_info/$', account_frames.person_info, name='person_info'),
        url(r'^frames/change-password/$', account_frames.change_password, name='change_password'),
        url(r'^frames/messages/$',account_frames.messages,name='messages'),
        url(r'^frames/my-items/$',account_frames.my_items,name='my_items'),
        url(r'^frames/logout/$',account_frames.logout,name='logout'),

        # Account frames for mobile
        url(r'^frames/mobile/person_info/$', mobile_account_frames.mobile_person_info, name='mobile_person_info'),
        url(r'^frames/mobile/change-password/$', mobile_account_frames.mobile_change_password, name='mobile_change_password'),
        url(r'^frames/mobile/messages/$',mobile_account_frames.mobile_messages,name='mobile_messages'),
        url(r'^frames/mobile/my-items/$',mobile_account_frames.mobile_my_items,name='mobile_my_items'),
        url(r'^frames/mobile/logout/$',mobile_account_frames.mobile_logout,name='mobile_logout'),
]
