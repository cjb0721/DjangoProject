from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    print("请求", request)
    return HttpResponse("首页")


def list(request):
    return HttpResponse("列表页")


"""
视图函数

"""