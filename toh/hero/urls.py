from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.hero_name, name='hero_name'),
    path('<int:id>/', views.hero_id, name='hero_id'),
    path('', views.index, name='index'),
]