import json
from json.decoder import JSONDecodeError
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Hero


# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def hero_id(request, id=None):
    return HttpResponse(f"Your id is {id}!")

def hero_name(request, name=""):
    return HttpResponse(f"Your name is {name}!")

# always return Json serialized data
@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        # safe=False to return list
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        # decode json data
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

@csrf_exempt
def hero_info(request, id=None):
    if request.method == "GET":
        hero = Hero.objects.get(id=id)
        # if we pass hero, it would not be serializable
        return JsonResponse({"id": id, "name": hero.name, "age": hero.age})
    elif request.method == "PUT":
        # decode json data
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest
        hero_found = Hero.objects.get(id=id)
        # update
        hero_found.name = hero_name
        hero_found.age = hero_age
        hero_found.save()
        return JsonResponse({"id": id, "name": hero_found.name, "age": hero_found.age}, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "PUT"])
