from django.db import models
from .rol_model import Rol
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    rol = models.CharField(max_length = 20)

    class Meta:
        app_label = 'usuarios'
