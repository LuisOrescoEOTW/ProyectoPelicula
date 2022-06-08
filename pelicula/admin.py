from django.contrib import admin
from .models import Director, Actor, Pelicula, Reseña, Administrador


# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Pelicula)
admin.site.register(Reseña)
admin.site.register(Administrador)


