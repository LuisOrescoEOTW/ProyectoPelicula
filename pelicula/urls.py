from django.urls import path
from . import views


urlpatterns = [
    path('', views.pelis, name='pelis'),
    path('actores', views.actore, name='actores'),     
    path('directores', views.directore, name='directores'),      
]
