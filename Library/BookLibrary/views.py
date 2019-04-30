from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from datetime import datetime, timedelta
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired

# Create your views here.


def index(request):
    # return HttpResponse("你好，世界！")
    messinfo = MessInfo.objects.all()
    hotpics = HotPic.objects.all().order_by('index')
    d = {'manager': 1, 'reader': 0}
    return render(request, 'BookLibrary/index.html', {'t': d, 'hotpics': hotpics, 'messinfo': messinfo})


def login(request, num):
    # print(num, type(num))

    user_dict = {}
    if num == '1':
        user_dict['user'] = "管理员"
        user_dict['load'] = "/booklibrary/login/manager/"
    else:
        user_dict['user'] = "读者"
        user_dict['link2'] = "注册"
        user_dict['load'] = "/booklibrary/login/"+num+'/'
    user_dict['link1'] = "返回"
    user_dict['id'] = int(num)
    if request.method == 'GET':

        return render(request, 'BookLibrary/login.html', {"use": user_dict})
    elif request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        request.session['username'] = name
        request.session.set_expiry(3600)
        # print(name, pwd)
        if user_dict['id'] == 1:
            if name == 'admin' and pwd == '123456':
                return redirect(reverse('booklibrary:manager'), {"user": name})
            else:
                return redirect(reverse('booklibrary:login', args=[num]))
        else:
            try:
                u = Users.objects.all().filter(name=name).filter(pwd=pwd)[0]
                return redirect(reverse('booklibrary:reader', args=[u.id]))
            except:
                return redirect(reverse('booklibrary:login', args=[num]))


def manager(request):
    return render(request, 'BookLibrary/manager.html')


def books(request):
    b = Books.objects.all()
    return render(request, 'BookLibrary/manager_books.html', {'books': b})


def books_add(request):
    if request.method == 'GET':
        return render(request, 'BookLibrary/manager_books_add.html')
    elif request.method == 'POST':
        # bid = request.POST['id']
        bname = request.POST['name']
        bauthor = request.POST['author']
        bcompany = request.POST['company']
        bdate = request.POST['date']

        b = Books()
        b.name = bname
        b.author = bauthor
        b.pub_com = bcompany
        b.pub_date = bdate
        b.save()

        return redirect(reverse('booklibrary:books'), {'books': Books.objects.all()})


def books_delete(request):
    if request.method == 'GET':
        return render(request, 'BookLibrary/manager_books_delete.html')
    elif request.method == 'POST':
        bid = request.POST['id']
        # print(bid, type(bid))
        Books.objects.get(pk=bid).delete()
        return redirect(reverse('booklibrary:books'), {'books': Books.objects.all()})


def book_info(request, id):
    b = Books.objects.get(pk=id)
    return render(request, 'BookLibrary/manager_book.html', {'book': b})


def book_modify(request, id):
    b = Books.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'BookLibrary/manager_book_modify.html', {'book': b})
    elif request.method == 'POST':
        b.name = request.POST['name']
        b.author = request.POST['author']
        b.pub_com = request.POST['company']
        b.pub_date = request.POST['date']
        b.save()
        return redirect(reverse('booklibrary:book_info', args=[id]), {'book': b})


def users(request):
    u = Users.objects.all()
    return render(request, 'BookLibrary/manager_users.html', {'users': u})


def manager_user(request, id):
    u = Users.objects.get(pk=id)
    return render(request, 'BookLibrary/manager_user.html', {'user': u})


def user_modify(request, id):
    u = Users.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'BookLibrary/manager_user_modify.html', {'user': u})
    elif request.method == 'POST':
        u.name = request.POST['username']
        u.pwd = request.POST['password']
        u.college = request.POST['college']
        u.num = request.POST['number']
        u.email = request.POST['email']
        u.save()
        return redirect(reverse('booklibrary:manager_user', args=[id]))


def user_delete(request, id):
    Users.objects.get(pk=id).delete()
    u = Users.objects.all()
    return redirect(reverse('booklibrary:users'), {'users': u})


def regist(request):
    if request.method == 'GET':
        return render(request, 'BookLibrary/regist.html')
    elif request.method == 'POST':
        pwd1 = request.POST['password']
        pwd2 = request.POST['password2']
        if pwd1 == pwd2:
            u = Users()
            u.name = request.POST['username']
            u.pwd = pwd1
            u.college = request.POST['college']
            u.num = request.POST['number']
            u.email = request.POST['email']
            u.save()
            id = Users.objects.get(num=u.num).id

            # 序列化id
            ser = Serializer(settings.SECRET_KEY, 100)
            resultid = ser.dumps({'userid': id}).decode('utf-8')  # 序列化对象转字符串对网址加密
            print(resultid)
            send_mail("用户注册", "<a href='http://127.0.0.1:8000/booklibrary/active/%s'>点我验证</a>" % (resultid, ),
                      settings.DEFAULT_FROM_EMAIL, [u.email, ])
            return redirect(reverse('booklibrary:login', args=[0]))
        else:
            return HttpResponse("两次输入密码不一致")


def reader(request, id):
    u = Users.objects.get(pk=id)
    return render(request, 'BookLibrary/reader.html', {'reader': u})


def reader_info(request, id):
    u = Users.objects.get(pk=id)
    return render(request, 'BookLibrary/reader_info.html', {'user': u})


def reader_modify(request, id):
    u = Users.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'BookLibrary/reader_modify.html', {'user': u})
    elif request.method == 'POST':
        u.name = request.POST['username']
        u.pwd = request.POST['password']
        u.college = request.POST['college']
        u.num = request.POST['number']
        u.email = request.POST['email']
        u.save()
        return redirect(reverse('booklibrary:reader', args=[id]))


def reader_query(request, id):
    u = Users.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'BookLibrary/reader_query.html', {'user': u})
    elif request.method == 'POST':
        item = request.POST.get('item')
        query = request.POST.get('query')
        # print(item, query)
        if item == 'name':
            b = Books.objects.filter(name=query)
        elif item == 'author':
            b = Books.objects.filter(author=query)
        return render(request, 'BookLibrary/reader_query.html', {'books': b, 'user': u})


def reader_books(request, uid, bid):
    # return HttpResponse("世界你好")
    u = Users.objects.get(pk=uid)
    b = Books.objects.get(pk=bid)
    if request.method == 'GET':
        return render(request, 'BookLibrary/reader_books.html', {'book': b,'user': u})
    elif request.method == 'POST':
        borrow = Borrows.objects.filter(book=b)[0]
        if borrow.status:
            return HttpResponse("此书已借出，请选择其它书籍")
        else:
            lb = borrow
            # print(datetime.now().date())
            # print(datetime.now().date()+timedelta(days=30))
            lb.date_return = datetime.now().date()+timedelta(days=30)
            lb.status = True
            lb.book = b
            lb.user = u
            lb.save()
            return render(request, 'BookLibrary/reader_books.html', {'book': b,'user': u, 'reader': lb})


def reader_historys(request, id):
    print("==================================")
    u = Users.objects.get(pk=id)
    borrow = Borrows.objects.filter(user=u)
    print(u)
    return render(request, 'BookLibrary/reader_borrow.html', {'user': u, 'histroys': borrow})


def reader_upload(request):
    if request.method == 'GET':
        return render(request, 'BookLibrary/reader_upload.html')
    elif request.method == 'POST':
        index = request.POST['index']
        pic = request.FILES['pic']
        pic = HotPic(index=index, pic=pic)
        pic.save()
        return redirect(reverse('booklibrary:index'))


def edit(request):
    if request.method == 'GET':
        return render(request, 'BookLibrary/edit.html')
    elif request.method == 'POST':
        title = request.POST['title']
        mess = request.POST['mess']
        msg = MessInfo(title=title, message=mess)
        msg.save()
        return redirect(reverse('booklibrary:index'))


def mail(request):
    send = settings.DEFAULT_FROM_EMAIL
    receive = ["1451055806@qq.com", "492595085@qq.com"]
    if request.method == 'GET':
        return render(request, 'BookLibrary/email.html', {'send': send, 'receive': receive})
    elif request.method == 'POST':
        title = request.POST['title']
        mess = request.POST['mess']
        try:
            send_mail(title, mess, send, receive)
            print("发送成功")
        except:
            return HttpResponse("发送失败")
        return redirect(reverse('booklibrary:index'))


def active(request, id):
    # 创建序列化对象 100s后过期
    dser = Serializer(settings.SECRET_KEY, 100)
    try:
        # 反序列化ID 将字符串转成对象
        obj = dser.loads(id)
        user = Users.objects.get(pk=obj['userid'])
        user.is_active = True
        user.save()
        return redirect(reverse('booklibrary:login', args=[0]))
    except SignatureExpired as e:
        return HttpResponse("连接失败")





