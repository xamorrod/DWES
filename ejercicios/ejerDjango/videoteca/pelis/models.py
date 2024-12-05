from django.db import models

# Create your models here.


class Director(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")

    def __str__(self):
        return f"{self.nombre} {self.apellidos} "


class Pelis(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Película")
    genero = models.CharField(max_length=100, verbose_name="Género")
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="director",
        verbose_name="director",
    )

    def __str__(self):
        return self.titulo



