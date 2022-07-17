from django.shortcuts import render
from django.db.models import Q
from .models import Director, Actor, Pelicula, Reseña
from django.http import HttpResponse


def pelis(request):    
    busqueda = request.GET.get("buscar")
    peliculasListados = Pelicula.objects.all()[:12]
    if busqueda:
        peliculasListados = Pelicula.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(puntaje__icontains = busqueda)
        ).distinct()
    
    #buscar = request.GET.get("buscarReseña")
    #if buscar:
    #    reseniasListados = Reseña.objects.filter(
    #        Q(pelicula__icontains = buscar)
    #    ).distinct()
    
    reseniasListados = Reseña.objects.all()
    
    return render(request, "base.html", {"peliculas": peliculasListados, "resenias": reseniasListados })

def actore(request):
    busquedaActores = request.GET.get("buscarAct")
    actoresListados = Actor.objects.all()
    if busquedaActores:
        actoresListados = Actor.objects.filter(
            Q(nombre__icontains = busquedaActores)|
            Q(nacionalidad__icontains = busquedaActores)
        ).distinct()
    return render(request, "actores.html", {"actores": actoresListados})

def directore(request):
    busquedaDirectores = request.GET.get("buscarDir")
    directoresListados = Director.objects.all()
    if busquedaDirectores:
        directoresListados = Director.objects.filter(
            Q(nombre__icontains = busquedaDirectores)|
            Q(nacionalidad__icontains = busquedaDirectores)
        ).distinct()
    return render(request, "directores.html", {"directores": directoresListados})