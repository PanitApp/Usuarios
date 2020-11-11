from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from usuarios.serializers.usuario_serializer import MyTokenObtainPairSerializer, CustomUserSerializer
from rest_framework import mixins
from rest_framework import generics
from usuarios.models.usuario_model import CustomUser
from rest_framework_simplejwt.backends import TokenBackend

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class HelloWorldView(APIView):

    def get(self, request):
        print(request.user.username)
        print(request.user.email)
        print(request.user.first_name)
        print(request.user.last_name)
        print(request.user.rol)
        return Response(data={"username":request.user.username, "email":request.user.email,"first_name":request.user.first_name,"last_name":request.user.last_name,"rol":request.user.rol}, status=status.HTTP_200_OK)

class UsuarioList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = CustomUser.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = CustomUser.objects.all()
        rol = self.request.query_params.get('rol', None)
        if rol is not None:
            queryset = queryset.filter(rol=rol)
        return queryset


class UsuarioDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            print(e)
