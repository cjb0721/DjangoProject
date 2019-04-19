from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    vid = request.POST['vote']
    qid = request.POST['qid']
    # print(vid, qid)

    s = Select.objects.get(pk=vid)
    print(s.vote, type(s.vote))
    s.vote += 1
    s.save()
    q = Question.objects.get(pk=qid)

    return HttpResponseRedirect('/polls/result/'+str(q.id)+'/', {})


def result(request, id):
    q = Question.objects.get(pk=id)
    return render(request, "polls/result.html", {'qs':q})






