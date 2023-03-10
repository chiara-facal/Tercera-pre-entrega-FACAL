from django.shortcuts import render

def index(request):
    return render(request, "AppCurso/index.html")

def registro_alumnos(request):
    return render(request, "AppCurso/alumnos.html")

def registro_profesores(request):
    return render(request, "AppCurso/profesores.html")

def entregables(request):
    return render(request, "AppCurso/entregables.html")
