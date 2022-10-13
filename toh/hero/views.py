import re
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    JsonResponse,
)
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")


def hero_id(request, id=0):
    return HttpResponse("Your id is %d!" % id)


def hero_name(request, name=""):
    return HttpResponse("Your name is %s!" % name)


@csrf_exempt
def hero_info(request, id=0):
    if request.method == "GET":
        hero = Hero.objects.get(id=id)
        return JsonResponse({"id": hero.id, "name": hero.name, "age": hero.age})
    elif request.method == "PUT":
        try:
            body = request.body.decode()
        except:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id=id)
        hero.name = json.loads(body)["name"]
        hero.age = json.loads(body)["age"]
        hero.save()
        response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(response_dict)
    else:
        return HttpResponseNotAllowed(["GET", "PUT"])


@csrf_exempt
def hero_list(request):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        try:
            body = request.body.decode()
            hero_name = json.loads(body)["name"]
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {"id": hero.id, "name": hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
