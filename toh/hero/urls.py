from django.urls import path
from . import views

urlpatterns = [path('', views.hero_list), path('<int:id>/', views.index_id, name='index_id'), path('<str:name>/', views.index_hero, name='index_hero'), path('info/<int:id>/', views.hero_info,name='hero_info')]