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
<<<<<<< HEAD
    path("autores/new", views.post_new, name="post_new"),
=======
>>>>>>> 8aa0859ac6daffea8d17c6ed910a9ba1bf24a8cd
]
