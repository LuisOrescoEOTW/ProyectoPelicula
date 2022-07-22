#ORM: Object Relational Mapping
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib import admin

class Director(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='Directores')
    año_nacimiento = models.DateField()
    resumen = models.CharField(max_length=300)

    class Meta():
        ordering = ['nombre']

    def __str__(self):
        return '{0}'.format(self.nombre)
    
    def admin_foto(self):
        return mark_safe('<img src="{}" with="130" height="100" />'.format(self.foto.url))
    admin_foto.short_description = 'Foto'
    admin_foto.allow_tags = True
        
class Actor(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='Actores')
    año_nacimiento = models.DateField()
    resumen = models.CharField(max_length=300)
    
    class Meta():
        ordering = ['nombre']

    def __str__(self):
        return '{0}'.format(self.nombre)
    
    def admin_foto(self):
        return mark_safe('<img src="{}" with="130" height="100" />'.format(self.foto.url))
    admin_foto.short_description = 'Foto'
    admin_foto.allow_tags = True

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    resumen = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='Peliculas')
    actores = models.ManyToManyField(Actor)
    año_realizacion = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.RESTRICT)    
    puntaje = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)]) #Promedio
    

    def admin_foto(self):
        return mark_safe('<img src="{}" with="130" height="100" />'.format(self.foto.url))
    admin_foto.short_description = 'Foto'
    admin_foto.allow_tags = True
    
    def actuaciones(self):
        return "; ".join([str(p) for p in self.actores.all()])
    actuaciones.short_description = 'actor/es'
    

    class Meta():
        ordering = ['-puntaje', 'nombre'] #Orden descendente por puntaje

    def actualizar(self):
        aux1 = 0
        aux2 = 0
        a = self.reseña_set.all()
        for i in a:
            aux1+=1
            aux2+=i.puntaje        
        resultado=0 if(aux2==0) else (aux2/aux1)
        self.puntaje = round(resultado)
        self.save()
        
    def __get_director(self):
        return Director.nombre

    def __str__(self):
        return '{0}'.format(self.nombre)
    
class Reseña(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=300)
    puntaje = models.IntegerField(default = 1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    mail = models.EmailField(max_length=200)
    aprobado = models.BooleanField(default=False)

    class Meta():
        ordering = ['pelicula']

    def save(self, *args, **kwargs):
        super(Reseña, self).save(*args, **kwargs)
        self.pelicula.actualizar()

    def actualization(self, *args, **kwargs):
        super(Reseña, self).save(*args, **kwargs)
        self.pelicula.actualizar()

    def __str__(self):
        return '{0}'.format(self.pelicula)

class Administrador(models.Model):    
    nombre = models.CharField(max_length = 300, blank = False)
    email = models.EmailField(max_length = 200)
    contraseña = models.CharField(max_length = 50, blank = False)
    
    def __str__(self):
        return '{0} {1} {2}'.format(self.nombre, self.email, self.contraseña)