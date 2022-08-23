from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppThatBeer.models import Cliente, Producto
from AppThatBeer.forms import ProductoFormulario

def cliente(request):
    cliente = Cliente(nombre='Jorge', apellido= 'Martinez', email= 'jorgemartinez@brewery.com.ar', direccion = 'Montes de Oca 661', provincia = 'Buenos Aires', cp = 1708, dni = 25628460)
    cliente.save()
    plantilla = loader.get_template('cliente.html')
    contexto = {
        "nombre" : cliente.nombre,
        "apellido": cliente.apellido,
        "email": cliente.email,
        "direccion": cliente.direccion,
        "provincia": cliente.provincia,
        "cp": cliente.cp,
        "dni": cliente.dni,
    
    }
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def clientes(request):
    return render(request, 'clientes.html')

def distribuidores(request):
    contexto = {
        'distribuidores': {
            'distribuidor1': 'Patagonia',
            'distribuidor2': 'Temple',
            'distribuidor3': 'Pentos',
            'distribuidor4': 'Pinta Point', 
            'distribuidor5': 'Prinston',
            'distribuidor6': 'Maldita Malta',
            'distribuidor7': 'Braavos Bar',

        }
    }
    return render(request, 'distribuidores.html', contexto)


def productos(request):
    productoslistado = Producto.objects.all()
    return render(request, 'productos.html', {"productos": productoslistado})

def inicio(request):
    return render(request, 'index.html')

def patrocinadores(request):
    return render(request, 'patrocinadores.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def noticias(request):
    return render(request, 'noticias.html')

def agregarcliente(request):
    return render(request, 'agregarcliente.html')

def agregardistribuidor(request):
    return render(request, 'agregardistribuidor.html')

def agregarpatrocinador(request):
    return render(request, 'agregarpatrocinador.html')

def agregarproducto(request):
    return render(request, 'agregarproducto.html')

def productoFormulario(request):
	if request.method == 'POST':
	    producto = Producto (request.POST['nombre'])
        producto.save()
        return render(request, 'productos.html')
    return render(request, 'agregarproducto.html')