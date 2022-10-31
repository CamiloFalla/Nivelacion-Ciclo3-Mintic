from tabnanny import verbose

from django.db import models


# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    cedula=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    tfno=models.CharField(max_length=10)
    
class Servicios(models.Model):
    nombre=models.CharField(max_length=50)
    especialidad=models.CharField(max_length=50)
    precio=models.IntegerField()
    
    def __str__(self):
        return self.nombre
    


class OrdenServicios(models.Model):
    numero:models.IntegerField()
    fecha=models.DateField(null=False)
    nombre_idServicios=models.ForeignKey(Servicios, on_delete=models.CASCADE)
    atendido=models.BooleanField()
    

class Oficio(models.Model):
    oficio_o=models.CharField(max_length=45,null=False)
    indicativo_o=models.CharField(max_length=45,null=False)
    
class Entidad_salud(models.Model):
    empresa_es=models.CharField(max_length=45,null=False)
    valor_es=models.IntegerField()
    nit=models.CharField(max_length=45,null=False)
    sector_productivo=models.CharField(max_length=45,null=False)
    fecha_creacion=models.DateTimeField(null=False)
    ciudad=models.CharField(max_length=45, verbose_name="Ciudad Sede Principal")
    direccion=models.CharField(max_length=45, null=True)
    telefono=models.CharField(max_length=45, null=True)
    
    def __str__(self):
        return 'El nombre es %s con Nit %s con pago mes %s' %(self.empresa_es, self.nit, self.valor_es)


    
class Condicion(models.Model):
    indicativo_c=models.CharField(max_length=45,null=False)
    condicion_c=models.CharField(max_length=45,null=False)   

class Transaccion(models.Model):
    costo_t=models.CharField(max_length=45,null=False)
    Entidad_salud_idEntidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)
    Oficio_idOficio=models.ForeignKey(Oficio, on_delete=models.CASCADE)
    fecha_t=models.DateField(null=False)
    descripcion_t=models.CharField(max_length=45,null=False)

class Usuarios(models.Model):
    nombres_u=models.CharField(max_length=45,null=True, verbose_name="Nombres")
    apellidos_u=models.CharField(max_length=45,null=True, verbose_name="Apellidos")
    documento_u=models.CharField(max_length=45,null=True,unique=True, verbose_name="Identificación")
    email_u=models.EmailField(unique=True)
    telefono_u=models.CharField(max_length=45,null=False)
    direccion_u=models.CharField(max_length=45,null=False)
    nombre_r=models.CharField(max_length=45,null=False)
    telefono_r=models.CharField(max_length=45,null=False)
    parentesco_r=models.CharField(max_length=45,null=False)
    documento_r=models.CharField(max_length=45,null=False)
    usuario_u=models.CharField(max_length=45,null=False,unique=True)
    password_u=models.CharField(max_length=45,null=False)
    Entidad_salud_idEntidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)
    Condicion_idCondicion=models.ForeignKey(Condicion,on_delete=models.CASCADE)
    Transaccion_idTransaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    

class Agendamiento(models.Model):
    idAgendamiento=models.IntegerField(primary_key=True,auto_created=True)
    horario_a=models.CharField(max_length=45,null=False)
    Usuarios_idUsuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Transaccion_idTransaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)

class Empleados(models.Model):
    idEmpleados=models.IntegerField(primary_key=True,auto_created=True)
    nombres_e=models.CharField(max_length=45,null=False)
    apellidos_e=models.CharField(max_length=45,null=False)
    documento_e=models.CharField(max_length=45,null=False,unique=True)
    email_e=models.EmailField(unique=True)
    telefono_e=models.CharField(max_length=45)
    direccion_e=models.CharField(max_length=45)
    tFecha_creacion=models.CharField(max_length=45,null=False)
    Agendamiento_ideAgendamiento=models.ForeignKey(Agendamiento, on_delete=models.CASCADE)
    Condicion_idCondicion=models.ForeignKey(Condicion,on_delete=models.CASCADE)
    Oficio_idOficio=models.ForeignKey(Oficio, on_delete=models.CASCADE)
