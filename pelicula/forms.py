from django import forms
from .models import Reseña

class MyForm(forms.ModelForm):
      class Meta:
        model = Reseña
        fields = ["pelicula", "comentario", "puntaje", "mail"]
        labels = {'pelicula': "Película", "comentario": "Comentario", "puntaje": "Puntaje", "mail": "@mail",}