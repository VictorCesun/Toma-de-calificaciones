from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    materias = models.ManyToManyField('Materia', related_name='alumnos')  # Relación muchos a muchos

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.matricula})"

class Docente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"Prof. {self.nombre} {self.apellido}"

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='materias')  # Un docente imparte varias materias

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} - {self.materia}: {self.calificacion}"

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField(default=True)

    def __str__(self):
        estado = "Presente" if self.presente else "Ausente"
        return f"{self.alumno} - {self.materia} ({self.fecha}): {estado}"
