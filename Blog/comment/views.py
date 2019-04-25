from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.


def comm(request, id):
    # return HttpResponse("评论成功")
    article = get_object_or_404(Article, pk=id)

    if request.method == "POST":
        commitform = Form(request.POST)
        if commitform.is_valid():
            commitform = commitform.save(commit=False)
            commitform.article = article
            commitform.save()
            return redirect(reverse('MyBlog:single', args=[id]))
        else:
            return HttpResponse("评论失败")
    else:
        return HttpResponse("没有内容")



