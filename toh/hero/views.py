from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello, World!')

def hero_id(request, id=0):
    return HttpResponse(f'Your id is {id}!')

def hero_name(request, name=""):
    return HttpResponse(f'Your name is {name}!')
