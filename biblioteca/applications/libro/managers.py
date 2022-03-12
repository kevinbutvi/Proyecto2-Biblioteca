# Se usa para convertir fecha para que no traiga errores
from contextlib import nullcontext
import imp
from datetime import datetime

from django.db import models
# Importacion para poder realizar consultas con operadores Logicos
from django.db.models import Count, Q
from django.contrib.postgres.search import TrigramSimilarity



class LibroManager(models.Manager):
    """ managers para el modelo Libro """

    def listar_libros(self):
        """ Manager para listar todos los libros """
        return (self.all())
    
    def listar_libros2(self, titulo, fecha_1, fecha_2):
        """ Manager para listar libros segun fecha de edicion """
        date1 = datetime.strptime(fecha_1, "%Y-%m-%d")
        date2 = datetime.strptime(fecha_2, "%Y-%m-%d")
        resultado = self.filter(
            titulo__icontains = titulo,
            fecha__range = (date1, date2)
            )
        return (resultado)
    
    def lista_libros_categoria(self, categoria):
        """ Manager para listar libros segun su categoria y ordena por titulo """
        resultado = self.filter(
            categoria__id = categoria
            ).order_by("titulo")
        return (resultado)

    def add_autor_libro(self, libro_id, autor):
        """ Manager para agregar autor segun ID de libro e ID de autor """
        libro = self.get(id = libro_id)
        libro.autores.add(autor)
        return (libro)

    def libro_num_prestamos(self):
        """ Manager para contar la cantidad de veces que se ha prestado x libro """ 
        resultado = self.aggregate(
            num_prestamos = Count("libro_prestamo")
        )
        return(resultado)

    def listar_libros_trg(self, titulo):
        """ Lista libros con filtros por trigram """
        if titulo:
            resultado = self.filter(
                titulo__trigram_similar = titulo,
            )
            return (resultado)
        else:
            return(self.all())

class CategoriaManager(models.Manager):
    """ Manager para el modelo Categorias """
    
    def categoria_por_autor(self, autor_id):
        """ Manager para listar categorias de libros por autor """
        resultado = self.filter(
            categoria_libro__autores__id = autor_id
        ).distinct() # Distinct para evitar resultados repetidos     
        return (resultado)
    
    def listar_categoria_libro(self):
        """ Manager para contar la cantidad de libros que hay en cada categoria """
        resultado = self.annotate(
            num_libros = Count("categoria_libro")
        )
        for item in resultado:
            print(" **************** ")
            print(item.nombre, item.num_libros)
        return(resultado)
