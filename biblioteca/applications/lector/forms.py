from mimetypes import init
from tkinter import Widget
from django import forms
from setuptools import Require
from applications.libro.models import Libro
from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    """ Formulario personalizado para prestamo """
    class Meta:
        """ El META hace que el html solo cree el form para estos 'fields' """
        model = Prestamo
        fields = (
            "lector",
            "libro",
        )


class MultiplePrestamoForm(forms.ModelForm):
    """ Formulario personalizado para prestamo de multiples libros CON CHECKBOX """
    
    libro = forms.ModelMultipleChoiceField(
        queryset = None,
        required = True,
        widget = forms.CheckboxSelectMultiple,
    )
    
    class Meta:
        """ El META hace que el html solo cree el form para estos 'fields' """
        model = Prestamo
        fields = (
            "lector",
        )
    
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        self.fields["libro"].queryset = Libro.objects.all()
    