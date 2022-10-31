from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View

from ControlIPS.forms import FormularioCrearServicio
from gestionServicios.models import Entidad_salud, Servicios


def pagina_principal(request):
        
    return HttpResponse("Prueba de funcionamiento")

def busqueda_servicios(request):
    
    return render(request, "Busqueda_servicio.html")

def buscar(request):
    
    if request.GET["srv"]:
        
        #mensaje="Servicio buscado: %r" %request.GET["srv"]
        servicio=request.GET["srv"]
        if len(servicio)>20:
            mensaje="Texto muy largo imposible buscar"
        else:
            servicios=Servicios.objects.filter(nombre__contains=servicio)
        
            return render(request, "resultado_busserv.html", {"servicios":servicios, "query":servicio})
        
    else:
        mensaje="No has introducido servicio"
        
    return HttpResponse(mensaje)

def entidad(request):
    
    if request.method=="POST":
        
        subject=request.POST["EPSnombre"]
        
        return render(request, "CargaInfoEPS.html")
    
    
    return render(request, "Entidad_salud.html")

def crearservicio(request):
    
    if request.method=="POST":
        nuevoServicio=FormularioCrearServicio(request.POST)
        
        if nuevoServicio.is_valid():
            infserv=nuevoServicio.cleaned_data
            datoserv=Servicios(nombre=infserv['nombre'], especialidad=infserv['especialidad'], precio=infserv['precio'])
            datoserv.save()
        
        return render(request, "CargaInfoEPS.html")
    
    else:
        nuevoServicio=FormularioCrearServicio()
    
    return render(request, "CargaServ.html", {"form":nuevoServicio})