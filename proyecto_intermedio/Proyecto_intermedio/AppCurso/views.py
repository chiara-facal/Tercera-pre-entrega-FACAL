from django.shortcuts import render
from AppCurso.models import Alumno, Profesor, Entregable

def index(request):
    return render(request, "AppCurso/index.html")

def registro_alumnos(request):

    alumnos_registrados = Alumno.objects.all()

    return render(request, "AppCurso/alumnos.html", {"alumnos_registrados": alumnos_registrados})

def registro_profesores(request):

    profesores_registrados = Profesor.objects.all()

    return render(request, "AppCurso/profesores.html", {"profesores_registrados": profesores_registrados})

def entregables(request):

    entrega_trabajo = Entregable.objects.all()

    return render(request, "AppCurso/entregables.html", {"entrega_trabajo": entrega_trabajo})
