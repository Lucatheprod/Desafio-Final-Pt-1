from django.urls import path
from AppThatBeer.models import Patrocinador
from AppThatBeer.views import aboutus, clientes, distribuidores, productos, patrocinadores, inicio, aboutus

urlpatterns = [
    path('', inicio, name= 'AppThatBeerInicio'),
    path('clientes', clientes, name= 'AppThatBeerClientes'),
    path('distribuidores', distribuidores, name= 'AppThatBeerDistribuidores'),
    path('patrocinadores', patrocinadores, name= 'AppThatBeerPatrocinadores'),
    path('productos', productos, name= 'AppThatBeerProductos'),
    path('sobrenosotros/', aboutus, name= 'AppThatBeerAboutUs'),

]