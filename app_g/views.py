from django.shortcuts import render
from users.models import Avatar
from app_g.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def inicio(request):
    try:
        avatares= Avatar.objects.get(user=request.user.id)
        imagen= avatares.imagen.url
    except:
        imagen=""

    return render(request, "app_g/index.html", {"url": imagen}) 
@login_required
def about(request):
    return render(request, "app_g/about.html")

def nada(request):
    return render(request, "app_g/nada.html")

def celularesNuevos(request):
    return render(request, "app_g/celularesNuevos.html")

class CursoListView(ListView):
     model = celular
     template_name = "celular_list.html"

class CursoDetailView(LoginRequiredMixin,DetailView):
    model = celular
    template_name = "app_g/celular_detalle.html"


class CursoCreateView(LoginRequiredMixin,CreateView):
     model = celular 
     success_url = reverse_lazy("lista")
     fields = "__all__"


class CursoUpdate(LoginRequiredMixin,UpdateView):
     model = celular
     success_url = reverse_lazy("lista")
     fields= ["nombre","email","modelo","descripcion","telefono", "precio", "estado", "imagen"]

class CursoDelete(LoginRequiredMixin,DeleteView):
     model = celular
     success_url = reverse_lazy("lista")
     template_name = "app_g/celular_confirm_delete.html"

#Celulares Nuevos
     
class celularNuevoListView(ListView):
     model = celularnuevo
     template_name = "celularnuevo_list.html"


class celularNuevoDetailView(LoginRequiredMixin,DetailView):
    model = celularnuevo
    template_name = "app_g/celularnuevo_detalle.html"


class celularNuevoCreateView(LoginRequiredMixin,CreateView):
     model = celularnuevo 
     success_url = reverse_lazy("listaNuevo")
     fields = "__all__"

class celularNuevoUpdate(LoginRequiredMixin,UpdateView):
     model = celularnuevo
     success_url = reverse_lazy("listaNuevo")
     fields= ["nombre","email","modelo","descripcion","telefono", "precio", "estado", "imagen"]

class celularNuevoDelete(LoginRequiredMixin,DeleteView):
     model = celularnuevo
     success_url = reverse_lazy("lista")
     template_name = "app_g/celularnuevo_confirm_delete.html"