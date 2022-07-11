from django.shortcuts import render
from django.db.models import Q
from .models import Director, Actor, Pelicula, Reseña



# Create your views here.



def pelis(request):
    busqueda = request.GET.get("buscar")
    peliculasListados = Pelicula.objects.all()[:12]
    if busqueda:
        peliculasListados = Pelicula.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(puntaje__icontains = busqueda)
        ).distinct()
    return render(request, "base.html", {"peliculas": peliculasListados})

def actore(request):
    busqueda = request.GET.get("buscar")
    actoresListados = Actor.objects.all()
    if busqueda:
        actoresListados = Actor.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(nacionalidad__icontains = busqueda)
        ).distinct()
    return render(request, "actores.html", {"actores": actoresListados})


