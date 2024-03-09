from django.urls import path
from app_g import views
from app_g.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about", views.about, name="about"),
    path("nada", views.nada, name="nada"),
    path("celulares_usados/ver", views.CursoListView.as_view(), name="lista"),
    path(r"^borrar/(?P<pk>\d+)$", views.CursoDelete.as_view(), name="Borrar"),
    path("celualres_usados/crear", views.CursoCreateView.as_view(), name="Crear"),
    path(r"^/(?P<pk>\d+)$", views.CursoDetailView.as_view(), name="Detalle"),
    path(r"^editar/(?P<pk>\d+)$", views.CursoUpdate.as_view(), name="Editar"),
   

]   

urlpatterns += [
path("celulares_nuevos/ver", views.celularNuevoListView.as_view(), name="ListaNuevo"),
path("celulares_nuevos/borrar", views.celularNuevoDelete.as_view(), name="BorrarNuevo"),
path("celulares_nuevos/crear", views.celularNuevoCreateView.as_view(), name="CrearNuevo"),
path("celulares_nuevo/detalles", views.celularNuevoDetailView.as_view(), name="Detallenuevo"),
path("celulares_nuevos/editar", views.celularNuevoUpdate.as_view(), name="EditarNuevo"),

  ]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)