from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
import os,json
from app01.models import *
from django.http import JsonResponse

# def index(request):
#     return render(request,'index.html')

def put(request):
    print(request.POST)
    file_obj = request.FILES.get("file")
    path = file_obj.name
    join_path = os.path.join("media","images",path)
    with open(join_path,"wb") as f_w:
        for line in file_obj:
            f_w.write(line)

    return HttpResponse("上传成功")

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

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        data = {
            'user': None,
            'msg': None,
            'code': '0',
        }
        user = request.POST.get("user").lower()
        pwd = request.POST.get("pwd").lower()
        if UserInfo.objects.filter(user=user,pwd=pwd):
            data['user'] = user
            data['msg'] = 'success'
            data['code'] = '200'
        else:
            data['msg'] = '用户名或者密码错误'
            data['code'] = '100'
        # json_data = json.dumps(data)
        # return HttpResponse(json_data)
        return JsonResponse(data)

def del_ajax(request):
    res = {
        "state": True,
        "code": 1000,
        "msg": None
    }
    try:
        pk = request.GET.get("pk")
        Book.objects.filter(pk=pk).delete()
        res['msg'] = 'success'
    except Exception as e:
        res['msg'] = e
        res['state'] = False
    return JsonResponse(res)