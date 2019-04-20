from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'vote/(\d+)/$', views.vote, name="vote"),
    url(r'detail/$', views.detail, name="detail"),
    url(r'result/(\d+)/$', views.result, name="result"),

    url(r'addquestion/$', views.addquestion, name='addquestion'),
    url(r'addquestionhander/$', views.addquestionhander, name='addquestionhander'),
    url(r'deletequestion/(\d+)/$', views.deletequestion, name='deletequestion'),
    url(r'modifyquestion/(\d+)/$', views.modifyquestion, name='modifyquestion'),
    url(r'modifyquestionhander/(\d+)/$', views.modifyquestionhander, name='modifyquestionhander'),

    url(r'votemanage/(\d+)/$', views.votemanage, name='votemanage'),
    url(r'addchoice/(\d+)/$', views.addchoice, name='addchoice'),
    url(r'addchoicehander/$', views.addchoicehander, name='addchoicehander'),
    url(r'deletechoice/(\d+)/$', views.deletechoice, name='deletechoice'),

]