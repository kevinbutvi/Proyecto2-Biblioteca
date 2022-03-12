from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import MultiplePrestamoForm, PrestamoForm
from .models import Prestamo




class AddPrestamo(FormView):
    """ Vista para Registrar nuevo prestamo """
        
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = "."

    def form_valid(self, form):
        # EL OBJETO QUE ES CREADO O RECUPERADO SE GUARDA EN LA VARIABLE "OBJ", Y EN "CREATED" SE ALMACENA UN BOOLEAN, si es que fue creado= True, si fue recuperada "false"
        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data["lector"],
            libro = form.cleaned_data["libro"],
            devuelto = False,
            defaults = {
                "fecha_prestamo": date.today() 
            }
        )
        
        if created:
            """ Condicional que define que si el legajo fue creado, sobreescribe la funcion, SINO redirije a pagina de error """
            return super(AddPrestamo, self).form_valid(form)
        else:
            return (HttpResponseRedirect("/"))


class AddMultiplePrestamo(FormView):
    """ Vista para prestar multiples libros desde una sola conexion con CheckBox """
    template_name = "lector/add_multiple_prestamo.html"
    form_class = MultiplePrestamoForm
    success_url = "." 

    def form_valid(self, form):
        """ Aca se recorre la lista de libros chequeados y se almacena en db """
        prestamos = []
        for l in form.cleaned_data["libro"]:
            prestamo = Prestamo(
                lector = form.cleaned_data["lector"],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto =  False
                )
            prestamos.append(prestamo)
        # Se usa BULK para hacer una sola conexion a la DB. Envia una lista de objetos
        Prestamo.objects.bulk_create(prestamos)
        return super(AddMultiplePrestamo, self).form_valid(form)
