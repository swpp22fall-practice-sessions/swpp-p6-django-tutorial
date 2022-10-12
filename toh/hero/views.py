import json

from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods

from hero.models import Hero


@csrf_exempt
@require_http_methods(["GET", "POST"])
def hero_list(request: HttpRequest):
    if request.method == "GET":
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == "POST":
        try:
            body = request.body.decode()
            body_dict = json.loads(body)
            hero = Hero.objects.create(**body_dict)
        except (json.JSONDecodeError, TypeError):
            return HttpResponseBadRequest
        data = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(data, status=201)


@csrf_exempt
@require_http_methods(["GET", "PUT"])
def hero_info(request: HttpRequest, id: int):
    try:
        hero = Hero.objects.get(id=id)
    except Hero.DoesNotExist:
        return HttpResponseBadRequest

    if request.method == "GET":
        data = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(data)
    elif request.method == "PUT":
        body = request.body.decode()
        body_dict = json.loads(body)
        for attr, value in body_dict.items():
            if attr not in {"name", "age"}:
                return HttpResponseBadRequest
            setattr(hero, attr, value)
        hero.save()
        data = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(data)


@require_GET
def echo_id(request: HttpRequest, id: int):
    return HttpResponse(f"Your id is {id}!")


@require_GET
def echo_name(request: HttpRequest, name: str):
    return HttpResponse(f"Your name is {name}!")
