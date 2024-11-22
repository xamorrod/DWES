from django.shortcuts import render

# Create your views here.


def principal(request):
    return render(request, "blog/principal.html")


def bienvenida(request):
    return render(request, "blog/bienvenida.html")
