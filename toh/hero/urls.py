from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.hero_id, name='id'),
    path('<str:name>/', views.hero_name, name='name'),
]
