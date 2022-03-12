from django.db import models

# Managers

from .managers import AutorManager


# Create your models here.

class Persona(models.Model):
    """Model definition for Persona."""
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()    
        
    def __str__(self):
        return (self.nombres + "-" + self.apellidos)
    
    class Meta:
        """Meta definition for Persona."""
        abstract = True


class Autor(Persona):
    """Model definition for Autor."""

    seudonimo = models.CharField("seudonimo", max_length=50, blank=True)
    objects = AutorManager()
    
    class Meta:
        """Meta definition for Autor."""
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
