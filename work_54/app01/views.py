from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from app01.models import *
def books(request):
    book_list = Book.objects.all()
    return render(request,'books.html',locals())

def add(request):
    if request.method == 'GET':
        return render(request,'add.html')
    else:
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish = request.POST.get('publish')
        author = request.POST.get('author')
        publish_date = request.POST.get('publish_date')

        book = Book.objects.create(title=title,price=price,publish=publish,author=author,publish_date=publish_date)
        print(book)
        return redirect('/books/')