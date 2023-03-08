from django.shortcuts import render

def index(request):
    return(render, "AppCurso/index.html")

def registro_alumnos(request):
    return(render, "AppCurso/alumnos.html")

def registro_profesores(request):
    return(render, "AppCurso/profesores.html")

def entregables(request):
    return(render, "AppCurso/entregables.html")
