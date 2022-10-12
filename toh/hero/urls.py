from django.urls import path
from . import views


urlpatterns = [
    path('', views.hero_list),
    path("<int:hero_id>/", views.hero_id, name="hero_id"),
    path("<str:hero_name>/", views.hero_name, name="hero_name"),
    path("info/<int:hero_id>/", views.hero_info, name="hero_info"),
]