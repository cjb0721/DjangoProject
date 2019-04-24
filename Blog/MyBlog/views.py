from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *
from django.core.paginator import *

# Create your views here.


def index(request):
    # print(request)
    # articles = Article.objects.all()
    new = Article.objects.all().order_by('-pub_date')
    # sort = ArticleSort.objects.all()
    # labels = Label.objects.all()
    # print(article, type(article))
    # print(article.title, article.sort, article.author, article.pub_date)
    # print(article.sort, type(article.sort))

    # 分页
    pageinator = Paginator(new, 4)
    num = request.GET.get('page')
    try:
        page = pageinator.page(num)
    except PageNotAnInteger:
        page = pageinator.page(1)
    except EmptyPage:
        page = pageinator.page(pageinator.num_pages)

    return render(request, 'MyBlog/index.html', {"pages": page, "new": list(new)[:3]})


def single(request, id):
    article = Article.objects.get(pk=id)

    comments = article.comment_set.all().order_by('-pub_date')
    new = Article.objects.all().order_by('-pub_date')
    # print("========================",list(new)[1].title)

    if request.method == 'GET':
        article.read_num += 1
        article.save()
        return render(request, "MyBlog/single.html", {"article": article, "comments": comments, "new": list(new)[:3]})
    elif request.method == 'POST':
        c = Comment()
        c.commentator = request.POST['name']
        c.email = request.POST['email']
        c.url = request.POST['url']
        c.content = request.POST['comment']
        c.article = article
        c.save()

        return redirect('/MyBlog/single/'+str(id)+'/', {"article": article, "comments": comments, "new": list(new)[:3]})

