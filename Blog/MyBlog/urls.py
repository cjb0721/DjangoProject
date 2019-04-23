from django.conf.urls import url, include
from . import views

app_name = 'MyBlog'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('single/$', views.single, name='single'),
]

