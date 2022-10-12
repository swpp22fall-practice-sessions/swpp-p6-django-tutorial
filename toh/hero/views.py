from django.forms import model_to_dict
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from json.decoder import JSONDecodeError

from django.views.decorators.csrf import csrf_exempt
from hero.models import Hero


def index(request):
    return HttpResponse("Hello, world!")


@csrf_exempt
def hero_list(request):
    queryset = Hero.objects.all()

    if request.method == 'GET':
        return JsonResponse(list(queryset.values()), safe=False)

    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=age)
        hero.save()
        response = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response, status=201)


@csrf_exempt
def hero_id(request, id=-1):
    queryset = Hero.objects.all()

    if request.method == 'GET':
        return JsonResponse(list(queryset.filter(id=id).values())[0], safe=False)

    elif request.method == 'PUT':
        try:
            hero = queryset.get(id=id)
            data = json.loads(request.body.decode())
            hero_name = data['name'] if 'name' in data else hero.name
            age = data['age'] if 'age' in data else hero.age
            hero.age = age
            hero.name = hero_name
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        hero.save()
        response = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response, status=201)
