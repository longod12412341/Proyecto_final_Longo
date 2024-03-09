from django import forms
from .models import *

class celularform(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    modelo = forms.CharField(label='Modelo', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    telefono = forms.CharField(label='Teléfono', max_length=20)
    precio = models.DecimalField(label='Precio',max_digits=20, decimal_places=2)
    estado = models.CharField(max_length=100,)
    imagen = models.ImageField(upload_to='imagenes/', null=True)

class celularNuevoform(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    modelo = forms.CharField(label='Modelo', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    telefono = forms.CharField(label='Teléfono', max_length=20)
    precio = models.DecimalField(label='Precio',max_digits=20, decimal_places=2)
    estado = models.CharField(max_length=100,)
    imagen = models.ImageField(upload_to='imagenes/', null=True)

class PostComentarioform(forms.ModelForm):
    
    class Meta:
        model= Comentario
        fields= ["content"]