from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    # url('index/', views.index),
    # url('index/$', views.index),
    url(r'^$', views.index, name='index'),
    url(r'list/$', views.list, name='list'),
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'delete/(\d+)/$', views.delete, name='delete'),
    url(r'addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'addherohander/$', views.addherohander, name='addherohander'),
]

