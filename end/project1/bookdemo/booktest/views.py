from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Hero,Book


def index(request):
    # 1加载模板
    # template = loader.get_template('index.html')
    # # 2构造上下文
    books = Book.objects.all()
    # context = {'books': books}
    # # 3渲染模板
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'index.html', {"books": books})



def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book': book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request, 'detail.html', {"book": book})

def about(request):
    return HttpResponse("这是关于页")