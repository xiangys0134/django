from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def index(request):
    class Book:
        def __init__(self,name,price,public,author,pub_date):
            self.name = name
            self.price = price
            self.public = public
            self.author = author
            self.pub_date = pub_date

    book1 = Book('红楼梦',200,'苹果出版社','alex','2012-12-02')
    book2 = Book('西游记',200,'苹果出版社','egon','2011-12-02')
    book3 = Book('水浒传',150,'苹果出版社','吴承恩','2012-12-02')
    book4 = Book('三国演义',220,'橘子出版社','bossjin','2015-12-02')

    book_list = [book1,book2,book3,book4]

    return render(request,'index.html',{"book_list":book_list})
