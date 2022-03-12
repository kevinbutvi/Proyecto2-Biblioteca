from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Libro


class ListLibros(ListView):
    """ Vista para listar libros con detalles y permite filtros de busqueda  segun fechas de edicion """
    context_object_name = "lista_libros"
    template_name = "libro/lista.html"

    def get_queryset(self):
        titulo = self.request.GET.get("input-titulo", "") 
        fecha1 = self.request.GET.get("input-fecha1", "")
        fecha2 = self.request.GET.get("input-fecha2", "") 
        if fecha1 and fecha2:
            return (Libro.objects.listar_libros2(titulo, fecha1, fecha2))
        else:
            return(Libro.objects.listar_libros())


class ListLibros2(ListView):
    """ Lista libro segun categoria pasada explicitamente en view """
    context_object_name = "lista_libros"
    template_name = "libro/lista2.html"

    def get_queryset(self):
        return (Libro.objects.lista_libros_categoria("2"))


class LibroDetailView(DetailView):
    """ Vista que muestra detalle de libro segun ID pasada por URL """
    model = Libro
    template_name = "libro/detalle.html"
    context_object_name = "libros"


class ListLibrosTrg(ListView):
    """ Lista libros y permite busqueda por trigram """
    context_object_name = "lista_libros"
    template_name = "libro/lista.html"

    def get_queryset(self):
        titulo = self.request.GET.get("input-titulo", "")
        return (Libro.objects.listar_libros_trg(titulo))
