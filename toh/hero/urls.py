from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.hero_name, name='hero_name'),
    path('<int:id>/', views.hero_id, name='hero_id'),
    path('info/<int:hero_id>/', views.hero_info, name='hero_info'),
    path('', views.hero_list, name='index'),
]