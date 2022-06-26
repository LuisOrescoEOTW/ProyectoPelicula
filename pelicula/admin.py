from django.contrib import admin
from .models import Director, Actor, Pelicula, Reseña



# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad', 'admin_foto', 'año_nacimiento',)
    search_fields = ('nombre', 'nacionalidad', 'año_nacimiento') #Buscar
    list_filter = ('nacionalidad',) #Añade filtros
    #list_editable = ('nombre', 'nacionalidad', 'año_nacimiento', 'resumen') #Editar campos
    #list_per_page = 3 #Paginación, solo 3 por página
   
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad', 'admin_foto', 'año_nacimiento', 'resumen',)
    search_fields = ('nombre', 'nacionalidad', 'año_nacimiento') #Buscar
    list_filter = ('nacionalidad',) #Añade filtros

class PeliculaAdmin(admin.ModelAdmin):    
    list_display = ('id', 'nombre', 'admin_foto', 'año_realizacion', 'actuaciones','director', 'puntaje')
    search_fields = ('nombre', 'actores', 'director') #Buscar
    list_filter = ('puntaje',) #Añade filtros

class ReseñaAdmin(admin.ModelAdmin):    
    list_display = ('id', 'pelicula', 'comentario', 'puntaje', 'mail', 'aprobado')
    search_fields = ('pelicula', 'mail') #Buscar
    list_filter = ('puntaje', 'aprobado') #Añade filtros


admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Reseña, ReseñaAdmin)


