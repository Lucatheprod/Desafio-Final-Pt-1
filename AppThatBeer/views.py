from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template, Context
from AppThatBeer.models import Cliente, Producto

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