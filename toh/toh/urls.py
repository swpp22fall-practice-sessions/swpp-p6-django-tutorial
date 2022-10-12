from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hero/', include('hero.urls')),
    path('admin/', admin.site.urls),
]
