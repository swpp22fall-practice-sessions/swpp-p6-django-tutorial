from django.urls import path

from . import views

urlpatterns = [
    path('', views.hero_list, name='hero_list'),
    path('info/<int:id>', views.hero_info, name='hero_info'),
    path('<int:id>', views.your_id, name='your_id'),
    path('<str:name>', views.your_name, name='your_name'),
]
