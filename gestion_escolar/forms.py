from django import forms
from django.contrib.auth.models import User
from .models import Alumno, Docente, Materia, Calificacion, Asistencia


# 📌 Formulario de Registro de Usuarios
class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


# 📌 Formulario para Alumnos
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['usuario', 'matricula', 'nombre', 'apellido', 'fecha_nacimiento']


# 📌 Formulario para Docentes
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['usuario', 'nombre', 'apellido']


# 📌 Formulario para Materias
class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'docente']


# 📌 Formulario para Calificaciones
class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['alumno', 'materia', 'calificacion']
        widgets = {
            'calificacion': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '100'}),
        }


# 📌 Formulario para Asistencia
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['alumno', 'materia', 'fecha', 'presente']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
