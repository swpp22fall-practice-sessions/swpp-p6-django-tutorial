from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def idView(request, id):
    return HttpResponse(f"Your id is {id}!")

def nameView(request, name):
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
                hero_age  = json.loads(body)['age']
          except (KeyError, JSONDecodeError) as e:
                return HttpResponseBadRequest()
          hero = Hero(name=hero_name, age=hero_age)
          hero.save()
          response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
          return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero_by_id = Hero.objects.get(pk=id)
        response_dict = {'id': hero_by_id.id, 'name': hero_by_id.name, 'age': hero_by_id.age}
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age  = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero_by_id = Hero.objects.get(pk=id)
        hero_by_id.name = hero_name
        hero_by_id.age  = hero_age
        hero_by_id.save()
        response_dict = {'id': hero_by_id.id, 'name': hero_by_id.name, 'age': hero_by_id.age}
        return JsonResponse(response_dict, status=201)