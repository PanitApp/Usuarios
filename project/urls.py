from django.urls import path, include

urlpatterns = [
    path('', include('usuarios.urls')),
]

