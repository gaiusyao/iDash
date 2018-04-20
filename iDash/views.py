from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'iDash/index.html', context={
        'title': 'iDash首页',
        'brand': 'iDash'
    })

def blog(request):
    return render(request, 'iDash/blog/blog.html', context={
        'title': '文章',
        'brand': 'iDash'
    })

