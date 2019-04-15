from django.shortcuts import render,redirect,HttpResponse
from app01 import models


# 展示出版社
def show_publisher(request):
    all_pub = models.Publisher.objects.all()
    return render(request,'show_pub.html',{'all_publisher':all_pub})


# 添加出版社
def add_publisher(request):
    err_msg,new_name = '',''
    if request.method == 'POST':
        new_name = request.POST.get('new_name','').strip()
        if not new_name:
            err_msg = '名称不能为空'
        obj_list = models.Publisher.objects.filter(name=new_name)
        if obj_list:
            err_msg = '名称已存在'
        if new_name and not obj_list:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher/')
    return render(request,'add_publisher.html',{'err_msg':err_msg,'new_name':new_name})


# 删除出版社
def del_publisher(request):
    pk = request.GET.get('pk')
    if models.Publisher.objects.filter(pk=pk):
        models.Publisher.objects.get(pk=pk).delete()
    else:
        return HttpResponse('非法请求')
    return redirect('/publisher/')


# 编辑出版社
def edit_publisher(request):
    err_msg, new_name = '', ''
    pk = request.GET.get('pk')
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        return HttpResponse('非法请求')

    obj = obj_list[0]
    if request.method == 'POST':
        new_name = request.POST.get('new_name','').strip()
        if not new_name:
            err_msg = '不能为空'

        obj_list = models.Publisher.objects.filter(name=new_name)
        if obj_list:
            err_msg = '名称已存在'

        if new_name and not obj_list:
            obj.name = new_name
            obj.save()
            return redirect('/publisher/')

    return render(request, 'edit_publisher.html', {'err_msg': err_msg, 'obj': obj})


# 展示图书
def show_books(request):
    all_books = models.Books.objects.all()
    return render(request, 'show_books.html', {'all_books': all_books})


# 添加图书
def add_books(request):
    all_pub = models.Publisher.objects.all()
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        models.Books.objects.create(name=book_name, pub_id=pub_id)
        return redirect('/show_books/')

    return render(request,'add_books.html',{'all_pub':all_pub})


# 删除图书
def del_books(request):
    del_id = request.GET.get('pk')
    models.Books.objects.get(pk=del_id).delete()
    return redirect('/show_books/')


# 编辑图书
def edit_books(request):
    edit_id = request.GET.get('pk')
    edit_obj = models.Books.objects.get(pk=edit_id)
    all_pub = models.Publisher.objects.all()
    if request.method == 'POST':
        edit_obj.name = request.POST.get('book_name')
        edit_obj.pub_id = request.POST.get('pub_id')
        edit_obj.save()
        return redirect('/show_books/')
    return render(request,'edit_books.html',{'edit_obj':edit_obj,'all_pub':all_pub})


# 展示作者
def show_authors(request):
    all_authors = models.Authors.objects.all()
    return render(request,'show_authors.html',{'all_authors':all_authors})


# 添加作者
def add_authors(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids')
        author_obj = models.Authors.objects.create(name=author_name)

        # 只支持第三张表是django自建的时候
        # author_obj.books.set(book_ids)

        # 第三张自己创建时:
        for book_id in book_ids:
            models.AuthorBook.objects.create(date='2018-01-18 07:39:24.390000',author_id=author_obj.pk,book_id=book_id)
        return redirect('/show_authors/')
    all_books = models.Books.objects.all()
    return render(request,'add_authors.html',{'all_books':all_books})


# 删除作者
def del_authors(request):
    pk = request.GET.get('pk')
    models.Authors.objects.filter(pk=pk).delete()
    return redirect('/show_authors/')


# 编辑作者
def edit_authors(request):
    pk = request.GET.get('pk')
    author_obj = models.Authors.objects.get(pk=pk)
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_ids = request.POST.get('book_ids')
        author_obj.name = author_name
        author_obj.save()
        author_obj.books.set(book_ids)
        return redirect('/show_authors/')
    all_books = models.Books.objects.all()
    return render(request,'edit_authors.html',{'author_obj': author_obj,'all_books':all_books})
