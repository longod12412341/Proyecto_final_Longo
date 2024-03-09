from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Avatar(models.Model):
   # Vincula con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{settings.MEDIA_URL} - {self.imagen}"

class User(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
