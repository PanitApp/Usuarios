from usuarios.models.usuario_model import Usuario
from usuarios.serializers.usuario_serializer import UsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
import ldap
import os

class UsuarioList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Usuario.objects.all()
        nombre_usuario = self.request.query_params.get('nombre_usuario', None)
        if nombre_usuario is not None:
            queryset = queryset.filter(nombre_usuario=nombre_usuario)
        return queryset


class UsuarioDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UsuarioLogin(mixins.RetrieveModelMixin,
                   generics.GenericAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        ldap_uri = os.environ.get('LDAP_URI')
        
        user = "uid=" + "difcortesgu" + "ou=users,dc=panitapp,dc=co"
        password = "admin"

        cnx = ldap.initialize(ldap_uri, bytes_mode=False)

        try:
            cnx.bind_s(user, password)
            print("Sirvio!!!!!")
        except ldap.SERVER_DOWN:
            print('LDAP server is not reachable')
        except ldap.INVALID_CREDENTIALS:
            print('Invalid LDAP credentials')

        return self.get(request, *args, **kwargs)

