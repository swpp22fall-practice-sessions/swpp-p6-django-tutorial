from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, world!\n')

def hero_id(request, id):
    return HttpResponse(f'Your id is {id}!\n')

def hero_name(request, name):
    return HttpResponse(f'Your name is {name}!\n')