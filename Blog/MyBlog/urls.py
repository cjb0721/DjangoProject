from django.conf.urls import url, include
from . import views

app_name = 'MyBlog'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('single/(\d+)/$', views.single, name='single'),
    url('catalog/(\d+)/$', views.catalog, name='catalog'),
    url('sorts/(\d+)/$', views.sorts, name='sorts'),
]

