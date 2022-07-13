from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('resen', views.resen, name='resen'),  
    path('', views.pelis, name='pelis'),
      
    path('actores', views.actore, name='actores'),     
    path('directores', views.directore, name='directores'),
=======
    path('', views.pelis),
    path('^actores$', views.actore),  
    #url(r'^controlpanel$', MenuAdministrador, name='controlpanel'),
>>>>>>> 8aec32f5109360c6f26f0949c02baea6c59c606c
]
