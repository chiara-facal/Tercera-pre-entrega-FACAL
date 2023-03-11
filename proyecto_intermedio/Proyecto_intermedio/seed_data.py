from AppCurso.models import Alumno, Profesor, Entregable

Alumno(nombre_completo = "Alumno 1",
curso = "Curso 1", 
email = "Email 1"
).save()

Alumno(nombre_completo = "Alumno 2",
curso = "Curso 2", 
email = "Email 2"
).save()

Alumno(nombre_completo = "Alumno 3",
curso = "Curso 3", 
email = "Email 3"
).save()

Profesor(nombre_completo = "Profesor 1",
curso = "Curso 1",
rol = "Rol 1",
profesion = "profesion 1"
).save()

Profesor(nombre_completo = "Profesor 2",
curso = "Curso 2",
rol = "Rol 2",
profesion = "profesion 2"
).save()

Profesor(nombre_completo = "Profesor 3",
curso = "Curso 3",
rol = "Rol 3",
profesion = "profesion 3"
).save()

Entregable(nombre_alumno = "Alumno 1",
nombre_entregable = "Entregable 1",
curso = "curso 1"
).save()

Entregable(nombre_alumno = "Alumno 2",
nombre_entregable = "Entregable 2",
curso = "curso 2"
).save()

Entregable(nombre_alumno = "Alumno 3",
nombre_entregable = "Entregable 3",
curso = "curso 3"
).save()