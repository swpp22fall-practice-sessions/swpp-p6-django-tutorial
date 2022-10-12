from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.echo_id, name="echo_id"),
    path("<str:name>/", views.echo_name, name="echo_name"),
]
