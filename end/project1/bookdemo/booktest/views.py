from django.shortcuts import render, redirect, reverse

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Hero, Book


def delete(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # redirect 重定向
    return redirect(to='/')


# def edithero(request, heroid):
#     hero = Hero.objects.get(id=heroid)
#     if request.method == 'GET':
#         return render(request, 'edithero.html', {"hero": hero})
#     elif request.method == 'POST':
#         hero.name = request.POST.get('heroname')
#         hero.content = request.POST.get("herocontent")
#         hero.gender = request.POST.get('sex')


def addhero(request, bookid):
    if request.method == 'GET':
        return render(request, 'addhero.html')
    elif request.method == 'POST':
        hero = Hero()
        hero.name = request.POST.get('heroname')
        hero.content = request.POST.get('herocontent')
        hero.gender = request.POST.get('sex')
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse('booktest:detail', args=(bookid,))
        return redirect(to=url)


def deletehero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)


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