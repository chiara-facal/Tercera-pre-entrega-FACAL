from django.shortcuts import render
from AppCurso.models import Alumno, Profesor, Entregable
from AppCurso.forms import AlumnoForm, ProfesorForm, TrabajoForm

def index(request):
    return render(request, "AppCurso/index.html")

def registro_alumnos(request):

    context = {
        "alumnos_registrados": Alumno.objects.all(),
        "Alumno": AlumnoForm(),
    }

    return render(request, "AppCurso/alumnos.html", context)

def registro_profesores(request):
    
    context = {
       "profesores_registrados": Profesor.objects.all(),
       "Profesor": ProfesorForm(),
    }


    return render(request, "AppCurso/profesores.html", context)

def entregables(request):
    
    context = {
        "entrega_trabajo": Entregable.objects.all(),
        "Entrega_trabajo": TrabajoForm(),
    }   

    return render(request, "AppCurso/entregables.html", context)
