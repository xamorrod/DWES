from django.shortcuts import render, get_object_or_404
from .models import Post, Autor
from .forms import PostForm , PostEdit
from django.http import HttpResponseRedirect

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


# Vista general para obtener autores
def autores(request):
    autores = Autor.objects.all().distinct()
    return render(request, "blog/autores.html", {"autores": autores})


# Vista con información del autor en concreto pasada su PK
def autores_detalle(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    posts_autor = Post.objects.filter(pk=autor.pk)

    return render(
        request,
        "blog/autores_detalle.html",
        {"autor": autor, "posts_autor": posts_autor},
    )


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        return HttpResponseRedirect("/thanks")
    else:
        form = PostForm()
    return render(request, "blog/abraham.html", {"form": form})


def post_new2(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            ftitulo = form.cleaned_data["titulo"]
            fcuerpo = form.cleaned_data["cuerpo"]
            fechaPublicado = form.cleaned_data["fechaPublicado"]
        autor = Autor.objects.get(id=1)
        Post.objects.create(
            titulo=ftitulo, autor=autor, cuerpo=fcuerpo, fechaPublicado=fechaPublicado
        )
        return render(request, "blog/post_added.html")

    else:
        form = PostForm()
    return render(request, "blog/abraham.html", {"form": form})


def post_edit(request, pk):
    if request.method == "POST":
        form = PostEdit(request.POST)
        if form.is_valid():
            ftitulo = form.cleaned_data["titulo"]
            fcuerpo = form.cleaned_data["cuerpo"]
            fechaPublicado = form.cleaned_data["fechaPublicado"]
        autor = Autor.objects.get(pk= 1)
        Post.objects.filter(pk=pk).update(
            titulo=ftitulo, autor=autor, cuerpo=fcuerpo, fechaPublicado=fechaPublicado
        )
        return render(request, "blog/post_added.html")

    else:
        form = PostEdit()
    return render(request, "blog/post_edit.html", {"form": form})
