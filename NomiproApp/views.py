from django.shortcuts import render, HttpResponse, redirect
from NomiproApp.forms import crear_Empleado, crear_Cargo, crear_Vinculacion, crear_Horario, ControlPagos, HorasExtras, HExtraxEmpleado, Parafiscales, ParafiscalesxEmpleados, Nominas
from .models import Empleados
# Create your views here.

def login(request):
    return render(request, "NomiproApp/login.html")

def inicio(request):
    return render(request, "NomiproApp/inicio.html")

def empleados(request):
    empleado=Empleados.objects.all()
    cxt={'empleado':empleado}
    return render(request, "NomiproApp/empleados.html",cxt)

def cargos(request):
    return render(request, "NomiproApp/cargos.html")

def vinculaciones(request):
    return render(request, "NomiproApp/vinculaciones.html")

def horarios(request):
    return render(request, "NomiproApp/horarios.html")

def parafiscales(request):
    return render(request, "NomiproApp/parafiscales.html")

def extras(request):
    return render(request, "NomiproApp/extras.html")

def control_Pago(request):
    return render(request, "NomiproApp/controlPago.html")

def nomina(request):
    return render(request, "NomiproApp/nomina.html")

def crearEmpleado(request):
    if request.method=="POST":
        nEmpleado = crear_Empleado(request.POST)
        if nEmpleado.is_valid():
            nEmpleado.save()
            return redirect("empleados")
    else:
        nEmpleado = crear_Empleado()
    return render(request, "NomiproApp/crearEmpleado.html", {"form":nEmpleado})

def crearCargo(request):
    if request.method=="POST":
        nCargo = crear_Cargo(request.POST)
        if nCargo.is_valid():
            enInfo = nCargo.cleaned_data
            return render(request, "gracias.html")
    else:
        nCargo = crear_Cargo()
    return render(request, "NomiproApp/crearCargo.html", {"form":nCargo})

def crearVinculacion(request):
    if request.method=="POST":
        nVinculacion = crear_Vinculacion(request.POST)
        if nVinculacion.is_valid():
            enInfo = nVinculacion.cleaned_data
            return render(request, "gracias.html")
    else:
        nVinculacion = crear_Vinculacion()
    return render(request, "NomiproApp/crearVinculacion.html", {"form":nVinculacion})

def crearHorario(request):
    if request.method=="POST":
        nHorario = crear_Horario(request.POST)
        if nHorario.is_valid():
            enInfo = nHorario.cleaned_data
            return render(request, "gracias.html")
    else:
        nHorario = crear_Horario()
    return render(request, "NomiproApp/crearHorario.html", {"form":nHorario})

def crearPagos(request):
    if request.method=="POST":
        nPagos = ControlPagos(request.POST)
        if nPagos.is_valid():
            enInfo = nPagos.cleaned_data
            return render(request, "gracias.html")
    else:
        nPagos = ControlPagos()
    return render(request, "NomiproApp/crearPagos.html", {"form":nPagos})

def crearHE(request):
    if request.method=="POST":
        nHE = HorasExtras(request.POST)
        if nHE.is_valid():
            enInfo = nHE.cleaned_data
            return render(request, "gracias.html")
    else:
        nHE = HorasExtras()
    return render(request, "NomiproApp/crearHE.html", {"form":nHE})

def crearExtEmp(request):
    if request.method=="POST":
        nExtEmp = HExtraxEmpleado(request.POST)
        if nExtEmp.is_valid():
            enInfo = nExtEmp.cleaned_data
            return render(request, "gracias.html")
    else:
        nExtEmp = HExtraxEmpleado()
    return render(request, "NomiproApp/crearExtEmp.html", {"form":nExtEmp})

def crearParafiscales(request):
    if request.method=="POST":
        nParafiscales = Parafiscales(request.POST)
        if nParafiscales.is_valid():
            enInfo = nParafiscales.cleaned_data
            return render(request, "gracias.html")
    else:
        nParafiscales = Parafiscales()
    return render(request, "NomiproApp/crearParafiscales.html", {"form":nParafiscales})

def crearParaEmp(request):
    if request.method=="POST":
        nParaEmp = ParafiscalesxEmpleados(request.POST)
        if nParaEmp.is_valid():
            enInfo = nParaEmp.cleaned_data
            return render(request, "gracias.html")
    else:
        nParaEmp = ParafiscalesxEmpleados()
    return render(request, "NomiproApp/crearParaEmp.html", {"form":nParaEmp})

def crearNomina(request):
    if request.method=="POST":
        nNomina = Nominas(request.POST)
        if nNomina.is_valid():
            enInfo = nNomina.cleaned_data
            return render(request, "gracias.html")
    else:
        nNomina = Nominas()
    return render(request, "NomiproApp/crearNomina.html", {"form":nNomina})