from django.shortcuts import render
from .models import Director, Pelis

# Create your views here.


def principal(request):
    return render(request, "pelis/index.html")


def directores(request):
    directores = Director.objects.all()
    return render(request, "pelis/directores.html", {"directores": directores})
