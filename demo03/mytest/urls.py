from django.conf.urls import url, include
from . import views

app_name = 'mytest'

urlpatterns = [
    url('^area/$', views.area, name='area'),
    url('^select/$', views.select, name='select'),
]
