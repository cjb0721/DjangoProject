from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader

# Create your views here.


def index(request):
    print("请求", request)
    # return HttpResponse("首页")
    # 1、加载模板
    indexpage = loader.get_template('booktest/index.html')
    body = {"username": "ggb"}
    # 2、使用变量渲染模板
    result = indexpage.render(body)
    # 3、返回模板
    return HttpResponse(result)


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
将函数和路由绑定
"""

"""
使用模板：
1、创建模板文件夹templates
2、配置模板目录 在settings.py中添加 os.path.join(BASE_DIR, 'templates')
3、创建项目模板目录，创建模板

    加载模板 temp = loader.get_template()
    使用变量渲染模板 result = temp.render({})
    返回模板  return HttpResponse(result)

"""


