from django.db import models


# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="Nombre")
    apellidos = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    dni = models.CharField(unique=True, max_length=9)
    # Blank true es para que sea opcional
    bio = models.TextField(blank=True, verbose_name="Biografía")

    #Clase para poner un poco más bonito 
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nombre


class Post(models.Model):

    # Añadir campos al modelo , no usar img , investigar

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fechaPublicado = models.DateField()
    # email = models.EmailField(unique=True, max_length=200)

    # Crear algún procedimiento en relación al modelo
    def __str__(self):

        return str(self.pk) + " " + self.titulo

    def calcularUser(self):
        return f"Este es el usuario: {self.autor[0:2]}{self.email[0:4]}"
