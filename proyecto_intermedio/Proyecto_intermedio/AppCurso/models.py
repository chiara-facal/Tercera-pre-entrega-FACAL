from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre_completo = models.CharField(max_length=40)
    curso = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    fecha_de_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Alumno: {self.nombre_completo}. Curso:{self.curso}'

class Profesor(models.Model): 
    nombre_completo = models.CharField(max_length=40)
    curso = models.CharField(max_length=30)
    rol = models.CharField(max_length=15)
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f'Profesor: {self.nombre_completo}. Curso: {self.curso}'

class Entregable(models.Model):
    nombre_alumno = models.CharField(max_length=40)
    nombre_entregable = models.CharField (max_length=30)
    curso = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Trabajo de: {self.nombre_alumno}. Curso: {self.nombre_entregable}'