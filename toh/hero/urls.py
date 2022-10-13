from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.hero_list),
    path("<int:id>/", views.id, name="id"),
    path("info/", views.hero_info),
    path("info/<int:id>/", views.hero_info),
    path("<slug:name>/", views.name, name="name"),
]
