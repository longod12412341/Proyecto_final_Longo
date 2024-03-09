from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from app_g.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
 
    path("login/", views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='Logout'),
    path("editar_usuario", views.editar_users, name="EditarUsuario"),
    path("agregar_avatar", views.agregar_avatar, name="AgregarAvatar"),
    
] 