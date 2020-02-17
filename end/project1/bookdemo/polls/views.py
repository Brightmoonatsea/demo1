from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request, "polls/index.html", {"questions": questions})


def detail(request, qid):
    try:
        question = Question.objects.get(id=qid)
        return render(request, "polls/detail.html", {"question": question})
    except:
        return HttpResponse("问题不合法")

    return HttpResponse("详情页"+qid)


def result(request, qid):
    return HttpResponse("结果页"+qid)

