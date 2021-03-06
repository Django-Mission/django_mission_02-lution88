from typing import List
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView

from .models import Post
# Create your views here.

def url_view(request):
    print('url_view()')
    data = {'code':'001', 'msg':'OK'}
    return HttpResponse('<h1>url_view</h1>')
    # return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == "GET":
        print(f'request.GET : {request.GET}')
    elif request.method == "POST":
        print(f'request.POST : {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'