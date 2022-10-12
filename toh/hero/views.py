from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero 

# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse("Hello, world!")

@csrf_exempt
def hero_id(request, id:int = 0):
    return HttpResponse(f"Your id is {id}!")

@csrf_exempt
def hero_name(request, name:str = ""):
    return HttpResponse(f"Your name is {name}!")

@csrf_exempt
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
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET''POST'])
 
@csrf_exempt   
def hero_info(request, id:int = 1):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        hero = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(hero, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_data = json.loads(body)
            hero_name = hero_data['name']
            hero_age = hero_data['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET''PUT'])