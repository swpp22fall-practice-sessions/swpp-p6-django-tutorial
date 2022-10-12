from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list, name='index'),
    path('<int:id>', views.hero_id, name='index'),
    path('<str:name>', views.hero_name, name='index'),
]