from django.shortcuts import render
from .models import Actor

# Create your views here.

def home(request):
    actoresListados = Actor.objects.all()
    return render(request, "gestionActores.html", {"actores": actoresListados})