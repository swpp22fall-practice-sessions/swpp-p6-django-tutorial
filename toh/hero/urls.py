from django.urls import path

from . import views

urlpatterns = [
    path("", views.hero_list, name="hero_list"),
    path("info/<int:id>/", views.hero_info, name="hero_info"),
    path("<int:id>/", views.echo_id, name="echo_id"),
    path("<str:name>/", views.echo_name, name="echo_name"),
]
