from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns=[
        url(r'^(?P<product_id>[0-9]+)/$',views.detail,name='detail'),
]
