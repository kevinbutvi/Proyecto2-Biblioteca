from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path(
        'libros/',
        views.ListLibros.as_view(),
        name="libros"
        ),
    path(
        'libros2/',
        views.ListLibros2.as_view(),
        name="libros2"
    ),
    path(
        'detalle_libros/<pk>/',
        views.LibroDetailView.as_view(),
        name="detalle_libros"
    ),
    path(
        'libros_trg',
        views.ListLibrosTrg.as_view(),
        name="libros_trg"
    ),
]