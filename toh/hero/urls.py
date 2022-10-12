from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list),
    path('info/<int:id>/', views.hero_info)
    # path('', views.index, name='index'),
    # path('<int:id>/', views.idView, name='hero_id'),
    # path('<str:name>/', views.nameView, name='hero_name')
]