from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from usuarios.views.rol_view import RolList
from usuarios.views.rol_view import RolDetail
from usuarios.views.usuario_view import UsuarioList
from usuarios.views.usuario_view import UsuarioDetail
from usuarios.views.usuario_view import UsuarioLogin

urlpatterns = [
    path('roles/', RolList.as_view()),
    path('roles/<int:pk>', RolDetail.as_view()),
    path('usuarios/', UsuarioList.as_view()),
    path('usuarios/<int:pk>', UsuarioDetail.as_view()),
    path('login/<int:pk>', UsuarioLogin.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)