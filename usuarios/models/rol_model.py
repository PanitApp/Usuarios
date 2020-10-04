from django.db import models

class Rol(models.Model):

    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 20)

    class Meta:
        app_label = 'usuarios'
