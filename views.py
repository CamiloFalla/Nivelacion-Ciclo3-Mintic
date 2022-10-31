from django.shortcuts import HttpResponse, render

# Create your views here.

def home(request):
    
    return render(request, "gestionServicios/Plantillas/home.html")

def EPS(request):
    
    return render(request, "gestionServicios/Plantillas/EPS.html")

def Empleado(request):
    
    return render(request, "gestionServicios/Plantillas/Empleado.html")

def User(request):
    
    return render(request, "gestionServicios/Plantillas/User.html")

def ServiciosEPS(request):
    
    return render(request, "gestionServicios/Plantillas/ServiciosEPS.html")

def MovimientosEPS(request):
    
    return render(request, "gestionServicios/Plantillas/MovimientosEPS.html")

def busqueda_servicios(request):
    
    return render(request, "busqueda_servicio.html")