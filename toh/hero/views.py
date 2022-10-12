from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero


def index(request):
    return HttpResponse("Hello, world!")


def hero_name(request, hero_name: str = ""):
    return HttpResponse(f"Your name is {hero_name}")


def hero_id(request, hero_id: int = None):
    return HttpResponse(f"Your id is {hero_id}")


@csrf_exempt
def hero_info(request, hero_id: int):
    if request.method == "GET":
        try:
            hero = Hero.objects.get(id=hero_id)
            hero_dict = {
                'id': hero.id,
                'age': hero.age,
            }
            return JsonResponse(hero_dict, safe=False)
        except:
            return HttpResponseBadRequest()
        pass
    elif request.method == "PUT":
        try:
            hero = Hero.objects.get(id=hero_id)
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero.name = hero_name
            hero.age = hero_age
            hero.save()
            hero_dict = {
                'id': hero.id,
                'name': hero.name,
                'age': hero.age,
            }
            return JsonResponse(hero_dict, safe=False)
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


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
        response_dict = { 'id': hero.id, 'name': hero.name }
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
