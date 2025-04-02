from django import forms
from django.contrib.auth.models import User
from .models import Alumno, Docente, Materia, Calificacion, Asistencia

# 📌 Formulario de Registro con selección de rol
class RegistroForm(forms.ModelForm):
    ROLES = [
        ('Alumno', 'Alumno'),
        ('Docente', 'Docente'),
        ('Administrativo', 'Administrativo'),
    ]
    
    rol = forms.ChoiceField(choices=ROLES, label="Rol")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'rol']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

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
