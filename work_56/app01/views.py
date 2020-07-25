from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app01.models import *

def bookadd(request):
    if request.method == 'GET':
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'addbook.html',locals())
    else:
        data =request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        data.pop("publish_id")
        data.pop("author_list")
        publish_id = request.POST.get("publish_id")
        author_list = request.POST.getlist("author_list")
        publish_obj = Publish.objects.filter(pk=publish_id).first()
        if publish_obj:
            book = Book.objects.create(**data,publish=publish_obj)
            #给书籍对象绑定作者
            book.author.set(author_list)
        else:
            print('出版社未选择')
        return redirect('/books/')

def authoradd(request):
    if request.method == 'GET':
        return render(request,'addauthor.html')
    else:
        data = request.POST.dict()
        birthday = request.POST.get("birthday")
        telephone = request.POST.get("telephone")
        addr = request.POST.get("addr")
        authordetail_obj = AuthorDetail.objects.create(birthday=birthday,telephone=telephone,addr=addr)
        data.pop("csrfmiddlewaretoken")
        data.pop("birthday")
        data.pop("telephone")
        data.pop("addr")
        Author.objects.create(**data,ad=authordetail_obj)

        return redirect("/bookadd/")
def publishadd(request):
    if request.method == 'GET':
        return render(request,'addpublish.html')
    else:
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        Publish.objects.create(**data)
        return redirect('/bookadd/')

def books(request):
    book_list = Book.objects.all()
    print(book_list)
    return render(request,'books.html',locals())


def delete(request,id):
    book = Book.objects.filter(pk=id).delete()
    print(book)
    return redirect('/books/')

def update(request,id):
    if request.method == 'GET':
        book = Book.objects.filter(pk=id).first()
        publish_list = Publish.objects.all()
        author_list = Author.objects.all()
        return render(request,'updatebook.html',locals())
    else:
        data =request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        data.pop("publish_id")
        data.pop("author_list")
        publish_id = request.POST.get("publish_id")
        author_list = request.POST.getlist("author_list")
        publish_obj = Publish.objects.filter(pk=publish_id).first()

        if publish_obj:
            book =Book.objects.filter(pk=id).update(**data,publish=publish_obj)
            #给书籍对象绑定作者
            Book.objects.filter(pk=id).first().author.set(author_list)
        else:
            print('出版社未选择')
        return redirect('/books/')