from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Avatar



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()

class Meta: 
    model = User
    fields= ["username", "email", "password1","password2"]
    help_text= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingreser su email:")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    #Opcional
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta: 
        model = User
        fields= [ "email", "last_name", "first_name" ,"password1","password2"]
        help_text= {k:"" for k in fields}
class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]

class Userform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)