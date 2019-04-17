from django.conf.urls import url
from . import views

urlpatterns = [
    # url('index/', views.index),
    # url('index/$', views.index),
    url(r'^$', views.index),
    url(r'list/$', views.list),
    url(r'detail/(\d+)/$', views.detail),
]

