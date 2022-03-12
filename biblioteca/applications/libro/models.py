from pickletools import optimize
from re import T
from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager
from django.db.models.signals import post_save
from PIL import Image

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    objects = CategoriaManager()
    
    def __str__(self):
        return (str(self.id) + " -/-/-/-/- " + self.nombre)


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria_libro") # "Related Name" sirve para hacer lo inverso al FK, es decir. Poder llegar desde la tabla "categoria" hasta la tabla "libro"
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField("Fecha de Lanzamiento")
    portada = models.ImageField(upload_to="portada", blank = True)
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    
    objects = LibroManager()
    
    
    
    def __str__(self):
        return (str(self.id) + " - " + self.titulo + "**" + str(self.fecha))


def optimize_image(sender, instance, **kwargs):
    """ Funcion para modificar parametros de imagen antes de almacenarla """
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)

post_save.connect(optimize_image, sender = Libro)
