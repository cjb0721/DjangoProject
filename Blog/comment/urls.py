from django.conf.urls import url, include
from . import views

app_name = "comment"

urlpatterns = [
    url('^comm/(\d+)/$', views.comm, name="comm"),
]

