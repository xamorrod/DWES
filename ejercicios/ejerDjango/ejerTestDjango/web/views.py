from django.shortcuts import render, get_object_or_404
from .models import Articulo


def principal(request):
    return render(request, "web/principal.html")


def vista_filtrada(request):

    articulos = Articulo.objects.all()
    return render(request, "web/principal.html", {"articulos": articulos})


def detalle_articulo(request, pk):
    articulos = get_object_or_404(Articulo, pk=pk)
    return render(request, "web/detalle_articulo.html", {"articulos": articulos})
