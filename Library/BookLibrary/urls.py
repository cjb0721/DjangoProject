from django.conf.urls import url, include
from . import views

app_name = "booklibrary"

urlpatterns = [
    url('^$', views.index, name="index"),
    url('login/(\d+)/$', views.login, name="login"),
    url('manager/$', views.manager, name="manager"),
    url('books/$', views.books, name="books"),
    url('books/add/$', views.books_add, name="books_add"),
    url('books/delete/$', views.books_delete, name="books_delete"),
    url('book/(\d+)/$', views.book_info, name="book_info"),
    url('book/modify/(\d+)/$', views.book_modify, name="book_modify"),

    url('manager/users/$', views.users, name="users"),
    url('manager/user/(\d+)/$', views.manager_user, name="manager_user"),
    url('user/modify/(\d+)/$', views.user_modify, name="user_modify"),
    url('user/delete/(\d+)/$', views.user_delete, name="user_delete"),

    url('regist/$', views.regist, name="regist"),
    url('reader/(\d+)/$', views.reader, name="reader"),
    url('reader_info/(\d+)/$', views.reader_info, name="reader_info"),
    url('reader_modify/(\d+)/$', views.reader_modify, name="reader_modify"),
    url('reader_query/(\d+)/$', views.reader_query, name="reader_query"),
    url('reader_books/(\d+)/(\d+)/$', views.reader_books, name="reader_books"),
    url('reader_historys/(\d+)/$', views.reader_historys, name="reader_historys"),



    # 上传图片
    url('reader_upload/$', views.reader_upload, name="reader_upload"),
    # 富文本编辑
    url('edit/$', views.edit, name="edit"),
    # 发送邮件
    url('mail/$', views.mail, name="mail"),
    url('active/(.*?)/$', views.active, name="active"),
    # Ajax异步刷新
    url('ajax/$', views.ajax, name="ajax"),
    url('ajaxs/$', views.ajaxs, name="ajaxs"),
    url('^ajaxlogin/$', views.ajaxlogin, name="ajaxlogin"),
    url('^checkuser/$', views.checkuser, name="checkuser"),
    url('^verifycode/$', views.verifycode, name="verifycode"),
]

