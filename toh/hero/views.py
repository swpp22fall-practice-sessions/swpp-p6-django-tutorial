from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from httplib2 import Http
import json
from json.decoder import JSONDecodeError


from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hellow World") 

def hero_id(request, id=0):
    return HttpResponse("Your id is " + str(id))

def hero_name(request, name=""):
    return HttpResponse("Your name is" + name)

@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

@csrf_exempt
def hero_info(request, id):
    if request.method == "GET":
        try:
            hero = Hero.objects.get(id = id)
        except Hero.DoesNotExist:
            return HttpResponseBadRequest()
        response_dict = {'id':hero.id, 'name': hero.name, 'age':hero.age}
        return JsonResponse(response_dict, status=200)
    elif request.method == "PUT":
        try:
            hero = Hero.objects.get(id = id)
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError, Hero.DoesNotExist) as e:
            return HttpResponseBadRequest()
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["PUT", "GET"])    
    

