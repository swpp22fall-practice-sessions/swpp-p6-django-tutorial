import json
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from hero.models import Hero

def index(request) :
    return HttpResponse('Hello, world!')

def hero_id(request, id: int) :
    return HttpResponse(f'Your id is {id}!')

def hero_name(request, name: str) :
    return HttpResponse(f'Your name is {name}!')

@csrf_exempt
def hero_list(request: HttpRequest) :
    if request.method == "GET" :
        herolist = Hero.objects.all().values()
        hero_all_list = []
        for hero in herolist :
            hero_all_list.append(hero)
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST' :
        try: 
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {
            'id': hero.id,
            'name': hero.name
        }
        return JsonResponse(response_dict, status=201)

    else :
        return HttpResponseBadRequest()

@csrf_exempt
def hero_info(request: HttpRequest, id: int) :
    if request.method == "GET" :
        try :
            hero = Hero.objects.get(id = id)
        except Hero.DoesNotExist :
            return HttpResponseBadRequest()
        return JsonResponse({
            "id": hero.id,
            "name": hero.name,
            "age": hero.age,
        })
    elif request.method == "PUT" :
        try: 
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
            hero = Hero.objects.get(id = id)
        except (KeyError, json.JSONDecodeError, Hero.DoesNotExist) as e:
            return HttpResponseBadRequest()
        except :
            return HttpResponseBadRequest()
        
        hero.name = hero_name
        hero.age = int(hero_age)
        hero.save()
        
        return JsonResponse({
            "id": hero.id,
            "name": hero.name,
            "age": hero.age,
        })
    return