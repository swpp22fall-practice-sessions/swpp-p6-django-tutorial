from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse("Hello, world!")


def echo_id(request: HttpRequest, id: int):
    return HttpResponse(f"Your id is {id}!")


def echo_name(requset: HttpRequest, name: str):
    return HttpResponse(f"Your name is {name}!")
