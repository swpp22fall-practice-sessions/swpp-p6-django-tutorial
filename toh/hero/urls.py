from django.urls import URLPattern, re_path as url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.hero_list, name='index'),
    path('<int:id>/', views.id, name='hero_id'),
    path('<str:name>/', views.name, name='hero_name'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
]