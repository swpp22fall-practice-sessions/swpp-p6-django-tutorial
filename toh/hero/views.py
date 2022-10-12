from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
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
            data = json.loads(body)
            hero_name = data['name']
            hero_age = data['age']
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
        try:
            hero = Hero.objects.get(id=id)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            return HttpResponseNotFound()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        try:
            hero = Hero.objects.get(id=id)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            return HttpResponseNotFound()
        try:
            body = request.body.decode()
            data = json.loads(body)
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero.name = data['name']
        hero.age = data['age']
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age}
        return JsonResponse(response_dict)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])