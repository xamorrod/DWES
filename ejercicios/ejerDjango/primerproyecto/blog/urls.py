from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="principal"),
    path("bienvenida", views.bienvenida, name="bienvenida"),
    path("filtrado", views.filtrado, name="filtrado"),
    path("detalle/<int:pk>", views.detalle, name="detalle"),
    # Url para obtener los autores y sus datos
    path("autores", views.autores, name="autores"),
    path("autores/<int:pk>", views.autores_detalle, name="detalle_autor"),
    path("post_new2", views.post_new2, name="post_new2"),
    path("post_added", views.post_new2, name="post_added"),
    path("post_edit/<int:pk>", views.post_edit, name="post_edit"),
]
