"""Proyecto_intermedio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AppCurso.views import index, registro_alumnos, registro_profesores, entregables, agregar_alumno, agregar_profesor, agregar_entrega

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "inicio"),
    path('registro-de-alumnos/', registro_alumnos, name="Registro-de-alumnos"),
    path('registro-de-profesores/', registro_profesores, name = "Registro-de-profesores"),
    path('entrega-de-tareas/', entregables, name="Entrega-de-tareas"),
    path('registro-de-alumnos/agregar', agregar_alumno, name="Agregar-alumno"),
    path('registro-de-profesores/agregar', agregar_profesor, name = "Agregar-profesor"),
    path('entrega-de-tareas/agregar', agregar_entrega, name="Agregar-trabajo")

]
