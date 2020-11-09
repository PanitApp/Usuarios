from django.urls import path, include
from django.contrib import admin 

urlpatterns = [
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls), 
]

