from django.urls import path
from AppThatBeer.models import Patrocinador
from AppThatBeer.views import aboutus, agregarcliente, agregardistribuidor, agregarpatrocinador, agregarproducto, clientes, distribuidores, noticias, productos, patrocinadores, inicio, aboutus, noticias

urlpatterns = [
    path('', inicio, name= 'AppThatBeerInicio'),
    path('clientes/', clientes, name= 'AppThatBeerClientes'),
    path('distribuidores/', distribuidores, name= 'AppThatBeerDistribuidores'),
    path('patrocinadores/', patrocinadores, name= 'AppThatBeerPatrocinadores'),
    path('productos/', productos, name= 'AppThatBeerProductos'),
    path('sobrenosotros/', aboutus, name= 'AppThatBeerAboutUs'),
    path('noticias/', noticias, name= 'AppThatBeerNoticias'),
    path('agregarcliente/', agregarcliente, name= 'AppThatBeerAgregarCliente'),
    path('agregardistribuidor/', agregardistribuidor, name= 'AppThatBeerAgregarDistribuidor'),
    path('agregarpatrocinador/', agregarpatrocinador, name= 'AppThatBeerAgregarPatrocinador'),
    path('agregarproducto/', agregarproducto, name= 'AppThatBeerAgregarProducto'),
    

]