from django.conf.urls import url, include
from . import views

app_name = "booklibrary"

urlpatterns = [
    url('^$', views.index, name="index"),
    url('login/(\d+)/$', views.login, name="login"),
    url('manager/$', views.manager, name="manager"),
    url('reader/$', views.reader, name="reader"),
]

