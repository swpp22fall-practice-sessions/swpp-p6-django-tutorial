from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError

from .models import Hero

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=name, age=age)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero = Hero.objects.filter(id=id).values()[0]
        return JsonResponse(hero, safe=False)
    elif request.method == 'PUT':
        hero = Hero.objects.get(id=id)
        try:
            body = request.body.decode()
            name = json.loads(body)['name']
            age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero.name = name
        hero.age = age
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])
