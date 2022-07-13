from django.urls import path
from . import views

urlpatterns = [
    path('resen', views.resen, name='resen'),  
    path('', views.pelis, name='pelis'),
      
    path('actores', views.actore, name='actores'),     
    path('directores', views.directore, name='directores'),
]
