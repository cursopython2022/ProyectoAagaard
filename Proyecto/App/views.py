from django.shortcuts import render
from App.forms import ArgentinoFormulario
from App.models import Argentino
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "App/inicio.html")

def argentino(request):
    return render(request, "App/argentino.html")

def extranjero(request):
    return render(request, "App/extranjero.html")

def nacionalizado(request):
    return render(request, "App/nacionalizado.html")

def argentinoFormulario(request):
    if request.method == 'POST':
        miFormulario = argentinoFormulario(request.POST) #Aquí me llega todo la info del html
        print(miFormulario)
        if miFormulario.is_valid(): #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            argentino = Argentino (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'])
            argentino.save()
            return render(request, "App/inicio.html") #podes volver a donde quieras, si vuelve al inicio es por que salio todo bien :)
    else:
        miFormulario= ArgentinoFormulario() #Formulario vacio para construir el html
    return render(request, "App/ArgentinoFormulario.html", {"miFormulario": miFormulario})
def extranjeroFormulario(request):
    if request.method == 'POST':
        miFormulario = extranjeroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            extranjero = extranjero (nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'])          
            extranjero.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = extranjeroFormulario()
    return render(request, "App/extranjeroFormulario.html", {"miFormulario": miFormulario})    
def nacionalizadoFormulario(request):
    if request.method == 'POST':
        miFormulario = nacionalizadoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nacionalizado = nacionalizado(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'])
            nacionalizado.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = nacionalizadoFormulario()
    return render(request, "App/nacionalizadoFormulario.html", {"miFormulario": miFormulario})                    


def busquedaArgentino(request):
    return render(request, "App/busquedaArgentino.html")

def buscarArgentino(request):
    if request.GET["dni"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        dni = request.GET['dni']
        argentinos = Argentino.objects.filter(dni__icontains=dni)

        return render(request, "App/resultadosPorBusquedaArgentino.html", {"argentinos":argentinos, "dni":dni})
    else:
        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)
