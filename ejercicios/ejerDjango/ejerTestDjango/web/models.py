from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
    