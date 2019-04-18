from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'vote/(\d+)/$', views.vote, name="vote"),
    url(r'detail/$', views.detail, name="detail"),
]