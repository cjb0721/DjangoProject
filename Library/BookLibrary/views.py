from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("你好，世界！")
    return render(request, 'BookLibrary/index.html')


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

    if request.method == 'GET':
        return render(request, 'BookLibrary/login.html', {"use": user_dict})
    elif request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['password']
        print(name, pwd)
        if name == 'admin' and pwd == '123456':
            return redirect(reverse('booklibrary:manager'), {"user": name})
        else:
            return redirect(reverse('booklibrary:login', args=[num]))


def manager(request):
    return render(request, 'BookLibrary/manager.html')


def reader(request):
    pass


