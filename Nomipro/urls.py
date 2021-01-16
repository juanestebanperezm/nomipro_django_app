"""Nomipro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from NomiproApp import views

urlpatterns = [
    
    path('login', views.login, name="login"),
    path('', views.inicio, name="inicio"),
    path('empleados/', views.empleados, name="empleados"),
    path('cargos', views.cargos, name="cargos"),
    path('vinculaciones', views.vinculaciones, name="vinculaciones"),
    path('horarios', views.horarios, name="horarios"),
    path('parafiscales', views.parafiscales, name="parafiscales"),
    path('extras', views.extras, name="extras"),
    path('control_Pago', views.control_Pago, name="control_Pago"),
    path('nomina', views.nomina, name="nomina"),
    path('crearEmpleado', views.crearEmpleado, name="crearEmpleado"), 
    path('crearCargo', views.crearCargo, name="crearCargo"),
    path('crearVinculacion', views.crearVinculacion, name="crearVinculacion"),
    path('crearHorario', views.crearHorario, name="crearHorario"),
    path('crearPagos', views.crearPagos, name="crearPagos"),
    path('crearHE', views.crearHE, name="crearHE"),
    path('crearExtEmp', views.crearExtEmp, name="crearExtEmp"),
    path('crearParafiscales', views.crearParafiscales, name="crearParafiscales"),
    path('crearParaEmp', views.crearParaEmp, name="crearParaEmp"),
    path('crearNomina', views.crearNomina, name="crearNomina"),
    
] 















