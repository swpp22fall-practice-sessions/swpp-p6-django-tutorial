from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.id, name='hero_id'),
    path('<str:name>/', views.name, name='hero_name'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
]