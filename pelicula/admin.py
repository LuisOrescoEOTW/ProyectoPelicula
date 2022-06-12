from re import search
from django.contrib import admin
from .models import Director, Actor, Pelicula, Reseña
from django.utils.html import format_html


# Register your models here.
#admin.site.register(Actor)
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nombre', 'nacionalidad', 'foto', 'fotos', 'año_nacimiento', 'resumen')
    search_fields = ('nombre', 'nacionalidad') #Buscar
    #list_editable = ('nombre', 'nacionalidad', 'año_nacimiento', 'resumen') #Editar campos
    list_filter = ('nacionalidad',) #Añade filtros
    #list_per_page = 3 #Paginación, solo 3 por página
    
    def fotos(self, obj):
        return format_html('<img scr=obj.foto.url width="130" height="100" />')



admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Reseña)


