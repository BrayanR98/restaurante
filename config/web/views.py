from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos,Empleados

# Create your views here.

#Todas las vistas son funciones de python
def Home(request):
    return render(request,'home.html')

def PlatosVista(request):
    #esta vista va usar un formulario django
    #debo crear un objeto de la clase formulario platos
    
    formulario = FormularioPlatos()
    
    #creamos un diccionario para enviar el formulario a html
    data = {
        'formulario' : formulario
    }
    #RESIVIMOS LOS DATOS DEL FORMULARIO
    if request.method =="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datoslimpios=datosFormulario.cleaned_data
            print(datoslimpios)
            #construir un diccionario de envio de datos a la bd
            platoNuevo=Platos(
                
                nombre=datoslimpios["nombre"],
                descripcion=datoslimpios["descripcion"],
                imagen=datoslimpios["fotografia"],
                precio=datoslimpios["precio"],
                tipo=datoslimpios["tipo"]
            )
            #intentare llevar mis datos a la BD
            try:
                platoNuevo.save()
                print("Exito guardando....")
            except Exception as error:
                print("upss",error)
            
    return render(request,'menuplatos.html',data)

def empleadosVista(request):
    formulario = FormularioEmpleados()
    data = {
        'formulario' : formulario
    }
    #RESIVIMOS LOS DATOS DEL FORMULARIO
    if request.method == "POST":
        datosFormulario = FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datoslimpios =datosFormulario.cleaned_data
            print(datoslimpios)
            empleadoNuevo= Empleados
    return render(request,'r.empleados.html',data)
