from django.http import HttpResponseBadRequest, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from json.decoder import JSONDecodeError
from .models import Hero

def index(request):
  return HttpResponse("Hello, world!")

def hero_id(request, id):
  return HttpResponse(f"Your id is {id}!")
def hero_name(request, name=""):
  return HttpResponse(f"Your name is {name}!")

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
    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def hero_info(request, id):
  if request.method == 'GET':
    target_hero = Hero.objects.get(id=id).values()
    return JsonResponse(target_hero)
    # try:
    # except:
    #   HttpResponseBadRequest()
  elif request.method == 'PUT':
    target_hero = Hero.objects.get(id=id)
    try:
      body = request.body.decode()
      hero_edit = json.loads(body)
    except (KeyError, JSONDecodeError) as e:
      return HttpResponseBadRequest()

    if hero_edit.get("name", None):
      target_hero.name = hero_edit["name"]
    if hero_edit.get("age", None):
      target_hero.age = hero_edit["age"]

    target_hero.save()
    response_dict = {'id': target_hero.id, 'name': target_hero.name, 'age': target_hero.age}
    return JsonResponse(response_dict)

  else:
    return HttpResponseNotAllowed(['GET', 'PUT'])