from django.shortcuts import render
from AppOne.models import *
from AppOne.forms import *
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request, 'AppOne/inicio.html')

# Formularios

def productos(request):

    if request.method == "POST":
 
            miform = Productosform(request.POST)
            print(miform)
 
            if miform.is_valid:
                  informacion = miform.cleaned_data
                  productos = Productos(nombre=informacion["nombre"], categoria=informacion["categoria"])
                  productos.save()
                  return render(request, "AppOne/inicio.html")
    else:
            miform = Productosform
 
    return render(request, "AppOne/productos.html", {"miform": miform})

def clientes(request):
    if request.method == "POST":
        miform = Clientesform(request.POST)
        if miform.is_valid():
            informacion = miform.cleaned_data
            clientes = Clientes(nombre=informacion["nombre"], dni=informacion["dni"], email=informacion["email"], fechacompra=informacion["fechacompra"])
            clientes.save()
            return render(request, "AppOne/inicio.html")
    else:
        miform = Clientesform()

    return render(request, 'AppOne/clientes.html', {"miform": miform})

def servicios(request):
    if request.method == "POST":
        miform = Serviciosform(request.POST)
        if miform.is_valid():
            informacion = miform.cleaned_data
            servicios = Servicios(nombre=informacion["nombre"], categoria=informacion["categoria"])
            servicios.save()
            return render(request, "AppOne/inicio.html")
    else:
        miform = Serviciosform()

    return render(request, 'AppOne/servicios.html', {"miform": miform})

#Formulario Busqueda

def busquedacategoria(request):
      
      return render(request, 'AppOne/busquedacategoria.html')



def buscar(request):
    categoria = request.GET.get("categoria") 

    if categoria:
        productos = Productos.objects.filter(categoria__icontains=categoria)
        servicios = Servicios.objects.filter(categoria__icontains=categoria)

        return render(request, 'AppOne/resultadosbusqueda.html', {'productos': productos, 'categoria': categoria, 'servicios': servicios})
    else:
        respuesta = 'No enviaste datos'
        return render(request, 'AppOne/resultadosbusqueda.html', {'respuesta': respuesta})
