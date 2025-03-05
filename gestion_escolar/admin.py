from django.contrib import admin
from .models import Alumno, Docente, Materia, Calificacion, Asistencia

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'apellido')
    search_fields = ('matricula', 'nombre', 'apellido')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'docente')

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'materia', 'calificacion', 'fecha')
    list_filter = ('materia',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'materia', 'fecha', 'presente')
    list_filter = ('materia', 'fecha', 'presente')
