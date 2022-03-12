import imp
from django.db import models 
# Importacion para poder realizar consultas con operadores Logicos
from django.db.models import Q




class AutorManager(models.Manager):
    """ Managers para el modelo Autor """

    def listar_autores(self):
        return (self.all())
    
    def buscar_autor(self, kword):
        resultado = self.filter(nombre__icontains = kword)
        return (resultado)
    
    def buscar_autor2(self, kword):
        # OR
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
            )
        return (resultado)
    
    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombre__icontains = kword
            ).exclude(
                Q(edad=81) | Q(nacionalidad__icontains = "chileno")
                )
        return (resultado)
    
    def buscar_autor4(self, kword):
        # AND
        resultado = self.filter(
            edad__gt = 50,
            edad__lt = 88
        ).order_by("apellidos")
        return (resultado)