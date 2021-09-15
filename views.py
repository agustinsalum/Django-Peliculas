from django import forms, http
from django.db import reset_queries
from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.http import HttpResponse
from cinefiloApp.forms import MiFormulario
from .models import Pelicula

# Create your views here.

def index(request):
    form = MiFormulario()
    peliculas = Pelicula.objects.all()
    return render (request, "miFormulario/formulario.html", {'form': form, "peliculas": peliculas})

def guardar(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST)
        form.save()
        return redirect('/')
    else:
        form = MiFormulario(request.post)
        return render (request, "miFormulario/formulario.html", {'form': form})