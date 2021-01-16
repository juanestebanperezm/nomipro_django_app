from django.db import models

# Create your models here.

class Cargos(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.CharField(max_length=15)
    valorCargo = models.FloatField()

    def __str__(self):
        return self.nombre

class Vinculaciones(models.Model):
    descripcion = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)

    def __str__(self):
        return self.descripcion
    
class Horarios(models.Model):
    tipoHorario = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)

    def __str__ (self):
        return self.tipoHorario

class Empleados(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField()
    telefono = models.IntegerField()
    tipoDocumento = models.CharField(max_length=45)
    numeroDocumento = models.CharField(max_length=45)
    idCargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    idVinculacion = models.ForeignKey(Vinculaciones, on_delete=models.CASCADE)
    idHorario = models.ForeignKey(Horarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ControlPagos(models.Model):
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    valorHorasExtras = models.FloatField()
    valorParafiscal = models.FloatField()
    mes = models.CharField(max_length=20)

class HorasExtras(models.Model):
    nombre = models.CharField(max_length=45)
    valor = models.FloatField()
    estado = models.CharField(max_length=15)

class HExtraxEmpleado(models.Model):
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    idHExtras = models.ForeignKey(HorasExtras, on_delete=models.CASCADE)
    numeroHoras = models.IntegerField()
    mes = models.CharField(max_length=15)
    
class Parafiscales(models.Model):
    nombre = models.CharField(max_length=45)
    valor = models.FloatField()
    estado = models.CharField(max_length=15)

class ParafiscalesxEmpleados(models.Model):
    idParafiscales = models.ForeignKey(Parafiscales, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    mes = models.CharField(max_length=20)

class Nominas(models.Model):
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    idCargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    idControlPago = models.ForeignKey(ControlPagos, on_delete=models.CASCADE)
    mes = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    subtotal = models.FloatField()
    total = models.FloatField()

#class acceso(models.Model):
#    usuario = models.EmailField()
#    clave = models.CharField(max_length=20)




