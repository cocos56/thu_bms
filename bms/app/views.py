from django.shortcuts import render


# Create your views here.

def index(request):
    # 获取请求方式
    print(request.method)
    # 获取URL里值
    print(request.GET)
    return render(request, 'index.html')
