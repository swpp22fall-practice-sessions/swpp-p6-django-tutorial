from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def id(request, id):
    return HttpResponse(f'Your id is {id}!')

def name(request, name):
    return HttpResponse(f'Your name is {name}!')