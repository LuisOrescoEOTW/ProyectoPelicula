from django.shortcuts import render
from .models import Director, Actor, Pelicula, Reseña

# Create your views here.

def pelis(request):
    peliculasListados = Pelicula.objects.all()[:12]
    return render(request, "base.html", {"peliculas": peliculasListados})