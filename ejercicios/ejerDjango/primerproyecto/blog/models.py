from django.db import models


# Create your models here.
class Post(models.Model):

    # Añadir campos al modelo , no usar img , investigar

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()
    fechaPublicado = models.DateField()
    email = models.EmailField(unique=True, max_length=200)

    # Crear algún procedimiento en relación al modelo
    def __str__(self):

        return str(self.pk) + " " + self.titulo 
    
    def calcularUser(self):
        return (f"Este es el usuario: {self.autor[0:2]}{self.email[0:4]}")
