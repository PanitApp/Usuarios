from rest_framework import serializers
from usuarios.models.usuario_model import Usuario
from usuarios.models.rol_model import Rol
from usuarios.serializers.rol_serializer import RolSerializer

class UsuarioSerializer(serializers.ModelSerializer):


    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuario', 'contrasena', 'nombres', 'email', 'rol']

    def create(self, validated_data):

        usuario = Usuario(nombre_usuario = validated_data.get("nombre_usuario"),
                          contrasena = validated_data.get("contrasena"),
                          nombres = validated_data.get("nombres"),
                          email = validated_data.get("email"),
                          rol = validated_data.get("rol"))
        usuario.save()
        return usuario

    def update(self, instance, validated_data):

        instance.nombre = validated_data.get("nombre")
        instance.contrasena = validated_data.get("contrasena")
        instance.nombres = validated_data.get("nombres")
        instance.email = validated_data.get("email")
        instance.rol = validated_data.get("rol")
        instance.save()
        return instance

    def to_representation(self, obj):

        data = super().to_representation(obj)

        rol = Rol.objects.get(id = data["rol"])
        rolSerializer = RolSerializer(rol)

        data["rol"] = rolSerializer.data

        return data
