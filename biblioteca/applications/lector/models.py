from django.db import models
from applications.lector.managers import PrestamoManager
from applications.libro.models import Libro
from applications.autor.models import Persona
from django.db.models.signals import post_delete


# Create your models here.

class Lector(Persona):
    """Model definition for Lector."""
    
    class Meta:
        """Meta definition for Lector."""
        
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE, related_name="lector_libro")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="libro_prestamo")
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()
    
    def save(self, *args, **kwargs):
        """ Sobreescritura del metodo SAVE para que reste sotck cuando carga un prestamo nuevo """
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)
    
    def __str__(self):
        return (self.libro.titulo + "  --->  " + self.lector.nombres)


def update_libro_stock(sender, instance, **kwargs):
    """ Funcion de prueba. SE EJECTUA CUANDO SE HACE UN DELTETE. Ver post_delete. (aumenta en 1 el stock cuando se elimina un "prestamo") """
    # la instancia es el modelo "Prestamo" en si mismo
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save() # se guardan los cambios en el modelo "prestamo"

# Lo siguiente es la instancia de post_delete. Como primer argumento se le pasa la funcion que queremos ejecutar, y como 2do argunmento se le pasa el MODELO sobre el cual vamos a trabajar, es decir, que cuando hagamos cambios en ese modelo, ahi se va a ejecutar la funcion
post_delete.connect(update_libro_stock, sender = Prestamo)
