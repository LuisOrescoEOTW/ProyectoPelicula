from ast import Delete
from asyncio.proactor_events import _ProactorDuplexPipeTransport
from multiprocessing.sharedctypes import Value
from string import punctuation
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Director(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField()
    año_nacimiento = models.DateField()
    resumen = models.CharField(max_length=300)

    class Meta():
        ordering = ['nombre']

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.nombre, self.nacionalidad, self.foto, self.año_nacimiento, self.resumen)

class Actor(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField()
    año_nacimiento = models.DateField()
    resumen = models.CharField(max_length=300)
    
    class Meta():
        ordering = ['nombre']

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.nombre, self.nacionalidad, self.foto, self.año_nacimiento, self.resumen)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    resumen = models.CharField(max_length=100)
    actores = models.ManyToManyField(Actor)
    año_realizacion = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.RESTRICT)    
    puntaje = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)]) #Puntaje general con todas las valoraciones
    
    class Meta():
        ordering = ['nombre']
    
    def save(self, punt, peli):
        list = Pelicula.objects.filter(Pelicula = peli)
        for lista in list:
            super().save(puntaje = punt)  

    def __get_actores(self):
        list = ""
        for actor in self.actores.all():
            list += Actor.nombre +"; "
        return list

    def __get_director(self):
        return Director.nombre

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.nombre, self.resumen, self.actores, self.año_realizacion, self.director)

class Reseña(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=300)
    puntaje = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    mail = models.EmailField(max_length=200)
    aprobado = models.BooleanField(default=False)

    class Meta():
        ordering = ['pelicula']

    def get_actualizar_puntaje(self, id):
        valoraciones=0
        puntajes=0
        lista_peliculas = Reseña.objects.filter(pelicula=id)
        for lista in lista_peliculas:
            valoraciones+=1
            puntajes+=lista.puntaje
        promedio = round(puntajes/valoraciones)
        Pelicula.save(promedio, self.pelicula)

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.pelicula, self.comentario, self.puntaje, self.mail, self.aprobado)

class Administrador(models.Model):    
    nombre = models.CharField(max_length = 300, blank = False)
    email = models.EmailField(max_length = 200)
    contraseña = models.CharField(max_length = 50, blank = False)
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.nombre, self.email, self.contraseña)