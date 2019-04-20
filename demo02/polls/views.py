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
    if 'vote' in request.POST:
        vid = request.POST['vote']
        qid = request.POST['qid']
        # print(vid, type(vid))
        if isinstance(vid, str):
            s = Select.objects.get(pk=vid)
            # print(s.vote, type(s.vote))
            s.vote += 1
            s.save()
            q = Question.objects.get(pk=qid)
            return HttpResponseRedirect('/polls/result/'+str(q.id)+'/', {})
        else:
            return HttpResponse("还没有投票")
    else:
        return HttpResponse("还没有选项信息")


def result(request, id):
    q = Question.objects.get(pk=id)
    return render(request, "polls/result.html", {'qs':q})


def addquestion(request):
    return render(request, 'polls/addquestion.html', {})


def addquestionhander(request):
    title = request.POST['title']
    print(title)
    q = Question()
    q.text = title
    q.save()
    return HttpResponseRedirect('/polls/', {'ql', Question.objects.all()})


def deletequestion(request, id):
    Question.objects.get(pk=id).delete()
    l = Question.objects.all()
    return HttpResponseRedirect('/polls/', {'ql': l})


def modifyquestion(request, id):
    q = Question.objects.get(pk=id)
    return render(request, 'polls/modifyquestion.html', {'qt': q})


def modifyquestionhander(request, id):
    qt = Question.objects.get(pk=id)
    qt.text = request.POST['title']
    qt.save()
    l = Question.objects.all()
    return HttpResponseRedirect('/polls/', {'ql': l})


def votemanage(request, id):
    q = Question.objects.get(pk=id)
    s = q.select_set.all()
    return render(request, 'polls/votemanage.html', {'question': q, 'sl': s})


def addchoice(request, id):
    q = Question.objects.get(pk=id)
    return render(request, 'polls/addchoice.html', {'qs': q})


def addchoicehander(request):
    q = Question.objects.get(pk=request.POST['qid'])
    sl = q.select_set.all()
    s = Select()
    s.item = request.POST['item']
    s.vote = request.POST['vote']
    s.question = q
    s.save()
    return HttpResponseRedirect('polls/votemanage/'+str(q.id)+'/', {'question': q, 'sl': sl})


def deletechoice(request, id):
    l = Select.objects.get(pk=id)
    q = l.question
    l.delete()
    sl = q.select_set.all()
    return HttpResponseRedirect('polls/votemanage/'+str(q.id)+'/', {'question': q, 'sl': sl})


def modifychoice(request, id):
    sl = Select.objects.get(pk=id)
    q = sl.question
    return render(request, 'polls/modifychoice.html', {'question': q, 'sl': sl})


def modifychoicehander(request, id):
    sl = Select.objects.get(pk=id)
    sl.item = request.POST['item']
    sl.vote = request.POST['vote']
    sl.save()
    q = sl.question
    return HttpResponseRedirect('/polls/votemanage/'+str(q.id)+'/', {'question': q, 'sl': sl})

