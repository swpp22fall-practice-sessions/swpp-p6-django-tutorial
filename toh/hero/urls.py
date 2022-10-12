from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('<int:id>/', views.id, name='id'),
    path('<str:name>/', views.name, name='name'),
    path('info/<int:id>/', views.hero_info, name="info")
]