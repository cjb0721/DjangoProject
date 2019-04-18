from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book,Hero
from django.template import loader

# Create your views here.


def index(request):
    print("请求", request)
    # return HttpResponse("首页")
    # # 1、加载模板
    # indexpage = loader.get_template('booktest/index.html')
    # body = {"username": "ggb"}
    # # 2、使用变量渲染模板
    # result = indexpage.render(body)
    # # 3、返回模板
    # return HttpResponse(result)
    return render(request, 'booktest/index.html', {"username": "ggb"})


def list(request):
    # return HttpResponse("列表页")
    book = Book.objects.all()
    return render(request, 'booktest/list.html', {'booklist': book})


def detail(request, id):
    # return HttpResponse("详情页"+str(id))
    book = Book.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': book})

    # try:
    #     book = Book.objects.get(pk=int(id))
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse("请输入正确ID")


def delete(request, id):
    try:
        Book.objects.get(pk=id).delete()
        book = Book.objects.all()
        # 使用render没有刷新请求URL
        # return render(request, 'booktest/list.html', {'booklist': book})
        # 使用HttpResponseRedirect重定向
        return HttpResponseRedirect(request, 'booktest/list.html', {'booklist': book})
    except:
        return HttpResponse("删除失败")


def addhero(request, id):
    try:
        # book = Book.objects.get(pk=id)
        return render(request, 'booktest/addhero.html', {"bid":id})
    except:
        return HttpResponse("添加失败")


def addherohander(request):
    bid = request.POST["bid"]
    hname = request.POST["heroname"]
    hgender = request.POST["sex"]
    hskill = request.POST["heroskill"]
    # print(bid, hname, hgender, hskill)
    # print(hgender, type(hgender))

    book = Book.objects.get(pk=bid)

    h1 = Hero()
    h1.name = hname
    h1.gender = True
    if hgender == "0":
        h1.gender = False
    h1.content = hskill
    h1.book = book
    h1.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bid)+'/', {"book": book})

    # return HttpResponse("提交成功")


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


