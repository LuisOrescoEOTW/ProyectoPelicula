from django.urls import path
from . import views

urlpatterns = [
    path('', views.pelis),
    path('^actores$', views.actore),  
    #url(r'^controlpanel$', MenuAdministrador, name='controlpanel'),
]
