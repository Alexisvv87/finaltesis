from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico

# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def Medicos(request):

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
            print(datos)



def Pacientes(request):

#Debo utilizar la clase formularioMedico
#CREAMOS ASI UN OBJETO
formulario1=Formulariopaciente()
diccionario={
    "formulario1":formulario1
}

#ACTIVAR LA RECEPCION DE DATOS
if request.method=='POST':
    #validar si los datos son correctos
    datosRecibidos=Formulariopaciente(request.POST)
    if datosRecibidos.is_valid():
        #capturamos los datos
        datos=datosRecibidos.cleaned_data
        print(datos)


return render(request,'Pacientes.html',diccionario)

