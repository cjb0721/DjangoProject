from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    # print(request)
    articles = Article.objects.all()
    # print(article, type(article))
    # print(article.title, article.sort, article.author, article.pub_date)
    # print(article.sort, type(article.sort))
    return render(request, 'MyBlog/index.html', {"articles": articles})


def single(request):
    article = Article.objects.get(pk=1)
    return render(request, "MyBlog/single.html", {"article": article})

