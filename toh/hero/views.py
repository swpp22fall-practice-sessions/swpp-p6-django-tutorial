import json
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Hero
from django.core.exceptions import ObjectDoesNotExist
@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except(KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest(e)
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        try:
            hero = Hero.objects.get(id=id)
        except (ObjectDoesNotExist) as e:
            return HttpResponseBadRequest(e)
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, safe=False)
    if request.method == 'PUT':
        try:
            hero = Hero.objects.get(id=id)
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (ObjectDoesNotExist, KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest(e)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, safe=False)