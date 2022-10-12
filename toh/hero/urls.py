from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:id>/', views.captureId, name='captureId'),
    path('<str:name>/', views.captureName, name='captureName'),
    
]
