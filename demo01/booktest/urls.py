from django.conf.urls import url
from . import views

urlpatterns = [
    # url('index/', views.index),
    # url('index/$', views.index),
    url(r'index/$', views.index),
    url(r'list/$', views.list),
]

