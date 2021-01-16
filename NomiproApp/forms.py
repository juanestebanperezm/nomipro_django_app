from django import forms
from .models import *


class crear_Empleado(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = [
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'tipoDocumento',
            'numeroDocumento',
            'idCargo',
            'idVinculacion', 
            'idHorario',                   
        ]
''' from django import forms

class crear_Empleado(forms.Form): #ok
    nombre=forms.CharField()
    apellido=forms.CharField()
    correo=forms.EmailField()
    telefono = forms.IntegerField()
    tipoDocumento = forms.CharField()
    numeroDocumento = forms.CharField()
    idCargo = forms.IntegerField()
    idVinculacion = forms.IntegerField()
    idHorario = forms.IntegerField() '''

class crear_Cargo(forms.Form): #ok
    nombre = forms.CharField()
    estado = forms.CharField()
    valorCargo = forms.FloatField()

class crear_Vinculacion(forms.Form): #ok
    descripcion = forms.CharField()
    estado = forms.CharField()
    
class crear_Horario(forms.Form): # ok
    tipoHorario = forms.CharField()
    hora = forms.CharField()

class ControlPagos(forms.Form): # ok
    idEmpleado = forms.IntegerField()
    valorHorasExtras = forms.FloatField()
    valorParafiscal = forms.FloatField()
    mes = forms.CharField()

class HorasExtras(forms.Form): # ok
    nombre = forms.CharField()
    valor = forms.FloatField()
    estado = forms.CharField()

class HExtraxEmpleado(forms.Form): # ok
    idEmpleado = forms.IntegerField()
    idHExtras = forms.IntegerField()
    numeroHoras = forms.IntegerField()
    mes = forms.CharField()
    
class Parafiscales(forms.Form): # ok 
    nombre = forms.CharField()
    valor = forms.FloatField()
    estado = forms.CharField()

class ParafiscalesxEmpleados(forms.Form): # ok
    idParafiscales = forms.IntegerField()
    idEmpleado = forms.IntegerField()
    mes = forms.CharField()

class Nominas(forms.Form): 
    idEmpleado = forms.IntegerField()
    idCargo = forms.IntegerField()
    idControlPago = forms.IntegerField()
    mes = forms.CharField()
    estado = forms.CharField()
    subtotal = forms.FloatField()
    total = forms.FloatField()
 