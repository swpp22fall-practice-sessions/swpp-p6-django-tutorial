from urllib import response
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
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
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name = hero_name)
        hero.save()
        response_dict = {'id':hero.id, 'name':hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id=""):
    if request.method == 'GET':
        myhero = Hero.objects.get(id=id)
        response_dict = {'id':myhero.id, 'name':myhero.name, 'age':myhero.age}
        return JsonResponse(response_dict, safe=False)
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            myhero = Hero.objects.get(id=id)
            myhero.name = json.loads(body)['name']
            myhero.age = json.loads(body)['age']
            myhero.save()
            response_dict = {'id':myhero.id, 'name':myhero.name, 'age':myhero.age}
            return JsonResponse(response_dict, status=201)
        except(KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])

# def index(request):
#     return HttpResponse('Hello world!')

# def hero_id(request, id=""):
#     return HttpResponse(f"Your id is {id}!")

# def hero_name(request, name=""):
#     return HttpResponse(f"Your name is {name}!")