from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="principal"),
    path("bienvenida", views.bienvenida, name="bienvenida"),
    path("filtrado", views.filtrado, name="filtrado"),
    path("detalle/<int:pk>", views.detalle, name="detalle"),
    path("autores", views.autores, name="autores"),
    path("autores/<str:autor>", views.autores_detalle, name="detalle_autor")
]
