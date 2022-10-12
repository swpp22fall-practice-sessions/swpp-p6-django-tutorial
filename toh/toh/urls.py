from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hero/', include('hero.urls')),
    path('admin/', admin.site.urls),
]
