from django.shortcuts import render, get_object_or_404
from .models import Post, Autor

# Create your views here.


def principal(request):
    context = Post.objects.all()
    return render(request, "blog/principal.html", {"posts": context})


def bienvenida(request):
    return render(request, "blog/bienvenida.html")


def filtrado(request):

    posts = Post.objects.all()
    autores = Post.objects.values_list("autor", flat=True).distinct()

    return render(request, "blog/filtrado.html", {"posts": posts, "autores": autores})


def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get()
    return render(request, "blog/detalle.html", {"post": post})


#Vista general para obtener autores
def autores(request):
    autores = Autor.objects.all().distinct()
    return render(request, "blog/autores.html", {"autores": autores})


#Vista con información del autor en concreto pasada su PK
def autores_detalle(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    posts_autor = Post.objects.filter(pk = autor.pk)
    
    return render(
        request,
        "blog/autores_detalle.html",
        {"autor": autor, "posts_autor": posts_autor},
    )
