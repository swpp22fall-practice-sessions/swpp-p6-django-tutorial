from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list, name="index"),
    path('<int:id>/', views.hero_info, name="hero_id"),
    path('<str:name>/', views.hero_name, name="hero_name"),
]
