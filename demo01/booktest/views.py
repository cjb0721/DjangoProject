from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.


def index(request):
    print("请求", request)
    return HttpResponse("首页")


def list(request):
    return HttpResponse("列表页")


def detail(request, id):
    # return HttpResponse("详情页"+str(id))
    try:
        book = Book.objects.get(pk=int(id))
        return HttpResponse(book)
    except:
        return HttpResponse("请输入正确ID")


"""
视图函数

"""