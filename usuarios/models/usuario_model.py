from django.db import models
from .rol_model import Rol

class Usuario(models.Model):

    id = models.AutoField(primary_key = True)
    nombre_usuario = models.CharField(max_length = 20 , unique=True)
    contrasena = models.CharField(max_length = 20)
    nombres = models.CharField(max_length = 50)
    email = models.EmailField()
    rol = models.ForeignKey(Rol, on_delete = models.CASCADE)

    class Meta:
        app_label = 'usuarios'
