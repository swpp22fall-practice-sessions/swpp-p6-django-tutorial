from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def captureId(request, id=0):
    return HttpResponse('Your id is %d' % id)

def captureName(request, name=""):
    return HttpResponse('Your name is %s' % name)