from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    # url('index/', views.index),
    # url('index/$', views.index),
    url(r'^$', views.index, name='index'),
    url(r'list/$', views.list, name='list'),
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'addbook/$', views.addbook, name='addbook'),
    url(r'addbookhander/$', views.addbookhander, name='addbookhander'),
    url(r'delete/(\d+)/$', views.delete, name='delete'),
    url(r'modifybook/(\d+)/$', views.modifybook, name='modifybook'),
    url(r'modifybookhander/(\d+)/$', views.modifybookhander, name='modifybookhander'),
    url(r'addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'modifyhero/(\d+)/$', views.modifyhero, name='modifyhero'),
    url(r'modifyherohander/(\d+)/$', views.modifyherohander, name='modifyherohander'),
    url(r'addherohander/$', views.addherohander, name='addherohander'),
]

