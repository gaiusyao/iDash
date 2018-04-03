from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'iDash/index.html', context={
                      'title': 'iDash首页', 
                      'brand': 'iDash'
                  })
