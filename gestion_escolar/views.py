from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegistroForm, AlumnoForm, DocenteForm, MateriaForm, CalificacionForm, AsistenciaForm
from .models import Alumno, Docente, Materia, Calificacion, Asistencia
from rest_framework import viewsets
from .serializers import AlumnoSerializer, CalificacionSerializer, DocenteSerializer, AsistenciaSerializer

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'auth/registro.html', {'form': form})

# Listar alumnos
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestion/lista_alumnos.html', {'alumnos': alumnos})

# Crear alumno
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'gestion/form_alumno.html', {'form': form})


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer