from django.http import HttpResponse
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json 
from json.decoder import JSONDecodeError
from .models import Hero

def index(request):
    return HttpResponse('Hello, world!')

def index_id(request, id):
    return HttpResponse("Your id is "+str(id)+"!")

def index_hero(request,name=""):
    return HttpResponse("Your name is "+name+"!")

def hero_list(request):
    if request.method == 'GET': 
        hero_all_list = [hero for hero in Hero.objects.all().values()] 
        return JsonResponse(hero_all_list, safe=False) 
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id':hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def hero_info(request, id):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        return JsonResponse({"id":hero.id, "name":hero.name, "age":hero.age })
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']

        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()

        hero = Hero.objects.get(id=id)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        return JsonResponse({"id":hero.id, "name":hero.name, "age":hero.age }, status=200)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])