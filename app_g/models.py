from django.db import models
from django.conf import settings
# Create your models here.

class celular(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    estado = models.CharField(max_length=100, null=True)
    imagen = models.ImageField(upload_to='celulares/', null=True)

    def __str__(self):
                return f" Nombre: {self.nombre} | Modelo: {self.modelo}| email: {self.email} | telefono: {self.telefono}"

class celularnuevo(models.Model):
    nombre = models.CharField(max_length=100, null= True)
    email = models.EmailField()
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=20, decimal_places=2,null=True)
    estado = models.CharField(max_length=100, null=True)
    imagen = models.ImageField(upload_to='celulares/', null=True)
    def __str__(self):
                return f" Nombre: {self.nombre} | Modelo: {self.modelo}| email: {self.email} | telefono: {self.telefono}"
    







# Comentarios para agregar, si es que tengo que volver a entregar y sino lo hago despues
class Comentario(models.Model):
    content = models.TextField(max_length=1000, help_text ="Ingrese un comentario")    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(celular, on_delete=models.CASCADE)

    class Meta:
           ordering= ["-post_date"]
    def __str__(self):
           len_title = 15 
           if len(self.content) > len_title:
                return self.content[:len_title] + "..."
           return self.content
        