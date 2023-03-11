from django import forms
from AppCurso.models import Alumno, Profesor, Entregable

class AlumnoForm(forms.ModelForm):
    class Meta: 
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta: 
        model = Profesor
        fields = "__all__"

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = "__all__"