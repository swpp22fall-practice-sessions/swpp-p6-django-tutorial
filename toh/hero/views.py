from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
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
def hero_info(request, id: int):
    if request.method == 'GET':
        hero = Hero.objects.get(id)
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    elif request.method == 'PUT':
        body = request.body.decode()
        request_data = json.loads(body)
        hero_name = request_data['name']
        hero_age = request_data['age']
        hero = Hero(name=hero_name, age=hero_age)
        hero.save()
    else:
        return HttpResponseNotAllowed(['GET''POST'])

def your_id(request, id: int):
    return HttpResponse(f'Your id is {id}!')

def your_name(request, name: str):
    return HttpResponse(f'Your name is {name}!')
