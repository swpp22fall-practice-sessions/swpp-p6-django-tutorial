from django.urls import path
from . import views
urlpatterns = [
    path('', views.hero_list),
    path('<int:id>/', views.captureId, name='captureId'),
    path('<str:name>/', views.captureName, name='captureName'),
    path('info/<int:id>/', views.hero_info, name='hero_info'),
]
