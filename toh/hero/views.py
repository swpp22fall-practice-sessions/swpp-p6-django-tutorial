from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
import json
from json.decoder import JSONDecodeError
from .models import Hero

# Create your views here.
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            heroName = json.loads(body)['name']
        except (KeyError, JSONDecodeError):
            return HttpResponseBadRequest()
        
        hero = Hero(name=heroName)
        hero.save()
        response_dict = { 'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, satuts=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def hero_info(request, id):
    if request.method == "GET":
        hero = Hero.objects.get(id=id)
        data = {
            "id": hero.id,
            "name": hero.name,
            "age": hero.age,
        }
        return JsonResponse(data, safe=False)
    elif request.method == "PUT":
        hero = Hero.objects.get(id=id)
        body = request.body.decode()
        hero.name = json.loads(body)['name']
        hero.age = json.loads(body)['age']
        hero.save()
        return JsonResponse(hero)