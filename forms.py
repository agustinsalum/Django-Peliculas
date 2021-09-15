from django import forms
from .models import Pelicula, Director
from django.forms import ModelChoiceField
from django import forms

class MiFormulario(forms.ModelForm):
    nombre      = forms.TextInput()
    director    = ModelChoiceField(queryset=Director.objects.all()) 
    elenco      = forms.TextInput()
    puntaje     = forms.IntegerField()


    class Meta:
        model = Pelicula
        fields = ['nombre','director', 'elenco', 'puntaje']

