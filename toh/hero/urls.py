from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero_list),
    path('<int:id>/', views.id, name='hid'),
    path('<str:name>/', views.name, name='hname'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
]