from django.contrib import admin

from gestionServicios.models import (Condicion, Empleados, Entidad_salud,
                                     Oficio, OrdenServicios, Servicios,
                                     Transaccion, Usuarios)

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display=("nombres_u", "apellidos_u", "documento_u")
    search_fields=("Nombres", "Apellidos")

class ServiciosAdmin(admin.ModelAdmin):
    list_filter=("especialidad",)

admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Entidad_salud)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Condicion)
admin.site.register(Transaccion)
admin.site.register(Oficio)
admin.site.register(OrdenServicios)
admin.site.register(Empleados)