from rest_framework import serializers
from usuarios.models.rol_model import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre']

