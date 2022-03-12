# Se usa para convertir fecha para que no traiga errores
import imp
from datetime import datetime

from django.db import models
# Importacion para poder realizar consultas con operadores Logicos
from django.db.models import Count, Q, Avg, Sum
from django.db.models.functions import Lower




class PrestamoManager(models.Manager):
    
    def edad_lector_libro(self):
        """ Manager que devuelve la edad promedio de los lectores que usaron cierto libro, en este caso, ID = 1"""
        resultado = self.filter(
            libro__id = "1"
        ).aggregate(
            prom_edad = Avg("lector__edad"), 
            sum_edad = Sum("lector__edad")
        )
        
        return(resultado)

    def num_libros_prestados(self):
        """ Manager que cuenta la cantidad de libros prestados de cada titulo"""
        # SE USA EL VALUES PARA AGRUPAR LA BUSQUEDA SEGUN ALGUN ATRIBUTO EN PARTICULAR *** Cuando se usa values, el retorno de la consutla en vez de ser un QuerySet es una lista de DICCIONARIOS con el valor de la busqeuda y la variable declarada en annotate**. --- Se pueden ir agregando tantos datos al diccionario como haga falta -- 
        resultado = self.values(
            "libro"
            ).annotate(
            num_prestados = Count("libro"),
            titulo = Lower("libro__titulo")
            )
        for item in resultado:
            print ("/////////")
            print (item, item["num_prestados"])
    
        return resultado