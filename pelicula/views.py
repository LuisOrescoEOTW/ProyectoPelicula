from django.shortcuts import render
from django.db.models import Q

import pelicula
from .models import Director, Actor, Pelicula, Reseña
#from django.http import HttpResponse
from django.contrib import messages
from .forms import MyForm

def my_form(request):
  try:
    if request.method == "POST":
      form = MyForm(request.POST)
      if form.is_valid():
        form.save()
        form = MyForm()
        messages.success(request, "Guardado correctamente")        
    else:
        form = MyForm()    
  except: 
    messages.error(request, "Hubo un error al guardar el artículo")  
  return render(request, "cv-form.html", {"form": form})
        
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
    
    #reseniasListados = Reseña.objects.select_related().filter(pelicula__Id = peliculasListados)
    
    reseniasListados = Reseña.objects.all()
    
    return render(request, "base.html", {"peliculas": peliculasListados, "resenias": reseniasListados},)

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