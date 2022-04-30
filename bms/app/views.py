from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app.models import Book
import json


# Create your views here.

def index(request):
    # 获取请求方式
    print(request.method)
    # 获取URL里值
    print(request.GET)
    return render(request, 'index.html')


def init_database(request):
    Book.objects.all().delete()
    book_list = []
    for i in range(1, 500001):
        b = Book(id=i, name='%d红楼梦' % i, author='曹雪芹', publisher='人民文学出版社', price=59.7, number=30)
        book_list.append(b)
    Book.objects.bulk_create(book_list)
    return HttpResponse('成功')


def books_info(request):
    if request.method == 'POST':  # 增加
        data = json.loads(request.body)
        Book(name=data['name'], author=data['author'], publisher=data['publisher'], price=data['price'],
             number=data['number']).save()
        return HttpResponse('添加图书成功')
    elif request.method == 'DELETE':  # 删除
        pass
    elif request.method == 'PUT':  # 修改
        pass
    elif request.method == 'GET':  # 查找
        req = dict(request.GET)
        page = int(req['page'][0])
        size = int(req['size'][0])
        _books_info = []
        for i in range((page - 1) * size + 1, page * size + 1):
            b = Book.objects.get(id=i)
            _books_info.append((b.id, b.name, b.author, b.publisher, b.price, b.number))
        return JsonResponse({
            'books_info': _books_info
        })
