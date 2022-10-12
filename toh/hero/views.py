from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

# Create your views here.
def index(request):
    return HttpResponse('Hello, world!\n')

def hero_id(request, id):
    return HttpResponse(f'Your id is {id}!\n')

def hero_name(request, name):
    return HttpResponse(f'Your name is {name}!\n')

@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero_score = json.loads(body)['score']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name, age=hero_age, score=hero_score)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
    if request.method == 'GET':
        hero_info = Hero.objects.get(id=id)
        return JsonResponse({'id': hero_info.id, 'name': hero_info.name, 'age': hero_info.age, 'score': hero_info.score})
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero_score = json.loads(body)['score']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(id=id, name=hero_name, age=hero_age, score=hero_score)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name, 'age': hero.age, 'score': hero.score}
        return JsonResponse(response_dict, status=201)