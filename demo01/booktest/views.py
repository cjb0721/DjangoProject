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


def addbook(request):
    try:
        return render(request, 'booktest/addbook.html', {})
    except:
        return HttpResponse("添加失败")


def addbookhander(request):
    bname = request.POST['bookname']
    # print(bname)
    b = Book()
    b.book_title = bname
    b.save()
    return HttpResponseRedirect('/booktest/list/', {'booklist': b})


def delete(request, id):
    try:
        Book.objects.get(pk=id).delete()
        book = Book.objects.all()
        # 使用render没有刷新请求URL
        # return render(request, 'booktest/list.html', {'booklist': book})
        # 使用HttpResponseRedirect重定向
        return HttpResponseRedirect('/booktest/list/', {'booklist': book})
    except:
        return HttpResponse("删除失败")


def modifybook(request, id):
    try:
        b = Book.objects.get(pk=id)
        return render(request, 'booktest/modifybook.html', {"book": b})
    except:
        return HttpResponse("跳转失败")


def modifybookhander(request, id):
    bname = request.POST['bookname']
    b = Book.objects.get(pk=id)
    b.book_title = bname
    b.save()
    return HttpResponseRedirect('/booktest/list/', {'booklist': b})


def addhero(request, id):
    try:
        # book = Book.objects.get(pk=id)
        return render(request, 'booktest/addhero.html', {"bid":id})
    except:
        return HttpResponse("添加失败")


def deletehero(request, hid):
    try:
        result = Hero.objects.get(pk=hid)
        book = result.book
        result.delete()
        return HttpResponseRedirect('/booktest/detail/'+str(book.id)+'/', {'book': book})
    except:
        return HttpResponse("添加失败")


def modifyhero(request, id):
    try:
        h = Hero.objects.get(pk=id)
        # print(h.id)
        return render(request, 'booktest/modifyhero.html', {"hero": h})
    except:
        return HttpResponse("跳转失败")


def modifyherohander(request, id):
    hname = request.POST['heroname']
    hgender = request.POST['sex']
    hcontent = request.POST['heroskill']
    bid = request.POST['bid']
    # print(hname, hgender, hcontent, bid)
    b = Book.objects.get(pk=bid)
    h = b.hero_set.get(pk=id)
    h.name = hname
    h.gender = hgender
    h.content = hcontent
    h.book = b
    h.save()
    return HttpResponseRedirect('/booktest/detail/'+str(bid)+'/', {'book': b})


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


