from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Select

# Create your views here.


def index(request):
    # return HttpResponse("index")
    l = Question.objects.all()
    return render(request, 'polls/index.html', {'ql': l})


def vote(request, id):
    q = Question.objects.get(pk=id)
    return render(request, 'polls/vote.html', {'qs':q, 'qid':id})


def detail(request):
    id = request.POST['item']
    qid = request.POST['qid']
    # print(id, qid)
    q = Question.objects.get(pk=qid)

    s = Select.objects.get(pk=id)
    # print(s.vote, type(s.vote))
    s.vote += 1
    s.save()
    return render(request, 'polls/detail.html', {'qs':q})


