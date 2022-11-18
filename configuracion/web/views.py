from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formulariopaciente import Formularipaciente

from web.models import Medicos
from web.models import Pacientes

# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def MedicosVista(request):

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
           #llevar mis datos hacia la BD
            medicoNuevo=Medicos(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                targeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"]
           )
            medicoNuevo.save()
            print("Exito ")
    return render(request,'registromedicos.html',diccionario)

def PacienteVista(request):

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=Formularipaciente()
    diccionario={
        "formulario":formulario
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=Formularipaciente(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
             #llevar mis datos hacia la BD
            PacienteVista=Pacientes(
                nombrepaciente=datos["nombrepaciente"],
                apellidospaciente=datos["apellidosPaciente"],
                cedulapaciente=datos["cedulaPaciente"],
                field_tipoafiliado=datos["TipoAfiliado"],
                field_regimen=datos["Regimen"],
                field_grupo_ingresos=datos["Grupo_ingresos"]
               
           )
            PacienteVista.save()
            print("Exito ")
    return render(request,'Pacientes.html',diccionario)
     


    

