from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from users.forms import AvatarFormulario
from users.models import Avatar
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.



def login_request(request):
    msg_login = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "app_g/index.html")
      
        msg_login = "Usuario o contraseña incorrectos"
    form = AuthenticationForm()
    return render (request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    msg_resgister =""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        #Creamos un nuevo user usando esos datos
        if form.is_valid:
            
            form.save()
            
            return render(request, "app_g/index.html", {"mensaje":"Usuario Creado"})
    msg_resgister ="Error en los datos ingresados"
     
    form=UserRegisterForm()
    return render(request, "users/registro.html", {"form": form})

@login_required
def editar_users(request):
    usuario=request.user

    if request.method == "POST":
        miFormulario= UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password1"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
            
            return render(request, "app_g/index.html")
    else:
        datos = {
            "first_name" : usuario.first_name,
            "email" : usuario.email
        }
        miFormulario = UserEditForm(initial=datos)
    return render(
        request,
        "users/editar_users.html",
        {
            "mi_form" : miFormulario,
            "usuario" : usuario
        }
    )


@login_required
def agregar_avatar(request):
    if request.method == "POST":
        mi_form = AvatarFormulario(request.POST, request.FILES)
        if mi_form.is_valid():
            user = User.objects.get(username=request.user)
            
            try:
                avatar = Avatar.objects.get(user=user) 
                
            except Avatar.DoesNotExist:
                avatar = Avatar(user=user, imagen=mi_form.cleaned_data["imagen"])
            else:
                avatar.imagen=mi_form.cleaned_data["imagen"]
            avatar.save()
            return render(request, "app_g/index.html")
    else:
        mi_form= AvatarFormulario()
    context_data = {"mi_form": mi_form}
    return render(request, "users/agregar_avatar.html", context_data)


#USUARIOS
