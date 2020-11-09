from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from usuarios.views.rol_view import RolList
from usuarios.views.rol_view import RolDetail
from usuarios.views.usuario_view import ObtainTokenPairWithColorView
from django.urls import path 
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from usuarios.views.usuario_view import ObtainTokenPairWithColorView, CustomUserCreate, HelloWorldView, LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')
]

urlpatterns = format_suffix_patterns(urlpatterns)