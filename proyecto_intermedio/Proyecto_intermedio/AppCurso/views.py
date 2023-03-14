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

def agregar_alumno(request):
    alumno_form = AlumnoForm(request.POST)
    alumno_form.save()
    context = {
        "alumnos_registrados": Alumno.objects.all(),
        "Alumno": AlumnoForm(),
    }

    return render(request, "AppCurso/alumnos.html", context)

def agregar_profesor(request):
    profesor_form = ProfesorForm(request.POST)
    profesor_form.save()
    context = {
       "profesores_registrados": Profesor.objects.all(),
       "Profesor": ProfesorForm(),
    }


    return render(request, "AppCurso/profesores.html", context)

def agregar_entrega(request):
    trabajo_form = TrabajoForm(request.POST)
    trabajo_form.save()
    context = {
        "entrega_trabajo": Entregable.objects.all(),
        "Entrega_trabajo": TrabajoForm(),
    }   

    return render(request, "AppCurso/entregables.html", context)

def buscar_alumnos(request):
    criterio = request.GET.get("criterio")
    context = {
        "personas": Alumno.objects.filter(nombre_completo__icontains=criterio).all()}

    return render(request, "AppCurso/alumnos.html", context)