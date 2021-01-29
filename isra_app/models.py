from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    def validacion(self, postData):
        errores = {}
        if len(postData['nombre']) == 0:
            errores['nombre'] = "Nombre  es obligatorio"
        EMAIL = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(postData['email']):
            errores['email'] = "email invalido"
        return errores

class User(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    objects = UserManager()